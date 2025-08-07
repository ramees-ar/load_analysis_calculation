# import requests
import json
from prefect import task
from prefect.cache_policies import NO_CACHE
from config_loader import load_config
from openapi_client import ApiClient,Configuration
from openapi_client.apis.tags.related_entities_api import RelatedEntitiesApi
from openapi_client.apis.tags import points_api,entities_v2_api
from openapi_client.model.list_v2_entities_by_relationships_payload import ListV2EntitiesByRelationshipsPayload

config = load_config()
model_id = "74aea58e-65cd-4314-b369-f270a589875e"

@task
def create_api_client():
    """
    Create an authenticated API client.
    """
    try:
        api_client_url = config["api"]["client"]["url"]
        api_client_password = config["api"]["client"]["password"]
        api_client_username = config["api"]["client"]["username"]
        configuration= Configuration(host=api_client_url,
            username=api_client_username,
            password=api_client_password,)
        api_client = ApiClient(configuration=configuration)
        return api_client
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@task
def create_points_api_client():
    """
    Create an authenticated API client.
    """
    try:
        api_client_url = config["api"]["points"]["url"]
        api_client_password = config["api"]["client"]["password"]
        api_client_username = config["api"]["client"]["username"]
        configuration= Configuration(host=api_client_url,
            username=api_client_username,
            password=api_client_password,)
        api_client = ApiClient(configuration=configuration)
        return api_client
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

@task(cache_policy=NO_CACHE)
def get_entity_nodes(api_client):
    try:
        related_entities_api = RelatedEntitiesApi(api_client)
        body = ListV2EntitiesByRelationshipsPayload(
            relationships=["component"],
            modelId=model_id  # Make sure model_id is defined globally or passed in
        )
        response = related_entities_api.list_v2_entities_by_relationships(body=body, skip_deserialization=True)

        if response.response.status >= 400:
            raise Exception(f"Error fetching data: {response.status_code}")

        # Ensure the response is parsed from raw JSON to Python objects
        return json.loads(response.response.data)

    except Exception as e:
        print(f"An error occurred while getting node: {e}")
        return []

@task(cache_policy=NO_CACHE)
def update_node(api_client,entityId,payload):
    try:
        entities_api = entities_v2_api.EntitiesV2Api(api_client)
        response = entities_api.update_v2_entity(path_params={"entityId":str(entityId)},body=payload)
        if response.response.status >= 400:
            raise Exception(f"Error fetching bills: {response.status_code}")
        return json.loads(response.response.data)
    except Exception as e:
        print(f"An error occurred from updating node: {e}")
        return None


@task(cache_policy=NO_CACHE)
def write_influx(api_client,payload):
    try:
        points_api_client = points_api.PointsApi(api_client)
        response = points_api_client.create_entity_historical_data(
            query_params={"appId": "659fdce64985a16e8b0366ea", "bucketType": "workflow",},
            body=payload,
            skip_deserialization=False
        )
        if response.response.status >= 400:
            raise Exception(f"Error fetching bills: {response.status_code}")
        print("write point result :  ", json.loads(response.response.data))
        return json.loads(response.response.data)
    except Exception as e:
        print(f"An error occurred from writing to influx: {e}")
        return None
