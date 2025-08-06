"""
Load Analysis Calculation Module

This module provides Prefect tasks for extracting motor data, computing load indicators, and writing results to InfluxDB.
It is designed to be used as part of a Prefect workflow for monitoring pump load and performance.
"""

from prefect import task
from datetime import datetime,timezone
from .api import create_points_api_client, create_api_client, get_entity_nodes, update_node, write_influx

# Maximum allowed values for normalization
MAX_CURRENT = 20.0         # Amps
MAX_VIBRATION = 10.0        # mm/s

@task
def extract_motor_data(data):
    """
    Extracts motor current and vibration data from a list of node objects.

    Args:
        data (list): List of node dictionaries, each possibly containing 'datasources'.

    Returns:
        list: List of dictionaries with extracted motor data and metadata.
    """
    result = []
    for obj in data:
        datasources = obj.get("datasources", [])  # Get datasources for each node

        motor_current = None
        motor_vibration = None

        # Extract motor current and vibration from datasources
        for ds in datasources:
            if(ds.get("motorCurrentAmp")):
                motor_current = ds.get("motorCurrentAmp")  # Get motor current if available
            if(ds.get("motorVibrationMMS")):
                motor_vibration = ds.get("motorVibrationMMS")  # Get motor vibration if available
                
        # Only include entries with both current and vibration data
        if motor_current is not None and motor_vibration is not None:
            extracted = {
                "id": obj.get("id"),  # Node ID
                "modelType": obj.get("meta", {}).get("modelType"),  # Model type from metadata
                "path": obj.get("meta", {}).get("path"),  # Path from metadata
                "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),  # Current UTC timestamp
                "motor_current": motor_current,  # Extracted motor current
                "motor_vibration": motor_vibration,  # Extracted motor vibration
            }
            result.append(extracted)  # Add to result list

    return result  # Return all extracted motor data

@task
def compute_load_indicators():
    """
    Main task to compute load indicators for all nodes.
    - Fetches node data from the API
    - Extracts motor data
    - Computes normalized load scores and status
    - Updates node status via API
    - Writes results to InfluxDB

    Returns:
        bool: True if successful
    """
    api_client = create_api_client()  # Create API client for node operations

    # Get parsed JSON data (list of dicts)
    raw_data = get_entity_nodes(api_client)  # Fetch node data from API

    # Extract relevant motor data from nodes
    motor_data = extract_motor_data(raw_data.get("nodes", []))
    for entry in motor_data:
        # Normalize current and vibration
        norm_current = entry["motor_current"] / MAX_CURRENT  # Normalize current to [0,1]
        norm_vibration = entry["motor_vibration"] / MAX_VIBRATION  # Normalize vibration to [0,1]

        # Compute weighted load percentage (0–100)
        load_percentage = round((0.6 * norm_current + 0.4 * norm_vibration) * 100, 2)

       # Status buckets based on load_percentage
        if load_percentage < 40:
            load_status = "Normal"
        elif load_percentage < 70:
            load_status = "Moderate"
        else:
            load_status = "High"
            
        # Update node with new load status
        node_update = {
            "loadIndicationStatus": load_status,
            "loadPercentage":load_percentage,
        }
        update_node(api_client,entry["id"],node_update)  # Update node in API
        
        # Prepare payload for InfluxDB write
        influx_write_payload = {
            "id": entry["id"],  # Node ID
            "timestamp": entry["timestamp"],  # Timestamp
            "modelType": entry["modelType"],  # Model type
            "path": entry["path"],  # Path
            "motor_current": entry["motor_current"],  # Motor current
            "motor_vibration": entry["motor_vibration"],  # Motor vibration
            "load_percentage": load_percentage,  # Computed load percentage
            "load_indication_status": load_status  # Status string
        }
        write_to_influx(influx_write_payload)  # Write to InfluxDB
    return True  # Indicate success

@task
def write_to_influx(data):
    """
    Writes the computed load indication status and related tags to InfluxDB.

    Args:
        data (dict): Dictionary containing all necessary fields and tags for InfluxDB.

    Returns:
        bool: True if successful
    """
    points_api_client = create_points_api_client()  # Create API client for points
    point_payload = {
            "tags": {
                "modelType": data.get("modelType"),  # Tag: model type
                "path": data.get("path"),  # Tag: path
                "vertexId": data.get("id"),  # Tag: node ID
            },
            "fields": {
                "loadIndicationStatus": {
                    "type": "string",
                    "value": data.get("load_indication_status")  # Field: load status
                },
                "loadPercentage": {
                    "type": "floatField",
                    "value": data.get("load_percentage")  # Field: load percentage
                },
            },
            "origin": data.get("timestamp"),  # Timestamp for the point
        }
    write_influx(points_api_client, point_payload)  # Write point to InfluxDB
    return True  # Indicate success
