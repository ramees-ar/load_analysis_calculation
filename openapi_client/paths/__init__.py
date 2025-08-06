# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    POINTS = "/points"
    POINTS_QUERY = "/points/query"
    RECORDS_SERVICE = "/records/{service}"
    RECORDS_SERVICE_RECORD_ID = "/records/{service}/{recordId}"
    ACTIVITY_MEASUREMENT = "/activity/{measurement}"
    ACTIVITY = "/activity"
    ENTITIES = "/entities"
    ENTITIES_ENTITY_ID = "/entities/{entityId}"
    ENTITIES_ENTITY_ID_CONNECTIONS = "/entities/{entityId}/connections"
    ENTITIES_ENTITY_ID_CONNECTIONS_CONNECTION_ID = "/entities/{entityId}/connections/{connectionId}"
    GRAPH_ENTITIES = "/graph/entities"
    GRAPH_ENTITIES_ENTITY_ID = "/graph/entities/{entityId}"
    GRAPH_ENTITIES_ENTITY_ID_LIST = "/graph/entities/{entityId}/list"
    GRAPH_ENTITIES_RELATIONSHIP_INFO = "/graph/entities/relationship/info"
    USERS_USER_ID_ROLE = "/users/{userId}/role"
    USERS_SEARCH = "/users/search"
    NOTIFY = "/notify"
    ROLES = "/roles"
    PERMISSIONS = "/permissions"
    PERMISSIONS_CHECK = "/permissions/check"
    MODULES = "/modules"
    MODULES_MODULE_ID = "/modules/{moduleId}"
