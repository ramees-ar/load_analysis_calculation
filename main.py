"""
Main entry point for the Pump Load Monitor Flow application.

This module orchestrates the pump load monitoring workflow using Prefect flows.
It imports the load analysis calculation module and executes the main workflow
to monitor pump performance indicators.
"""

import sys
import os
from prefect import flow

# Add the parent directory to the Python path to enable imports from sibling directories
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the load analysis calculation function from the load_analysis_calculation module
from load_analysis_calculation.load_analysis import compute_load_indicators

# --------------------
# Main Prefect Flow
# --------------------
@flow(name="Pump Load Indicator Workflow")
def pump_load_indicator_flow():
    """
    Main Prefect flow that orchestrates the pump load monitoring process.
    
    This flow:
    1. Starts the pump load indicator process
    2. Calls the compute_load_indicators function to analyze motor data
    3. Prints the result for monitoring purposes
    
    Returns:
        The result from the compute_load_indicators function
    """
    print("[main.py] Starting pump load indicator process")
    
    # Execute the load analysis calculation task
    duration_output = compute_load_indicators()
    
    # Log the result for monitoring and debugging
    print("checkout result", duration_output)
    
    return duration_output


# Entry point when the script is run directly
if __name__ == "__main__":
    # Execute the main pump load indicator workflow
    pump_load_indicator_flow()