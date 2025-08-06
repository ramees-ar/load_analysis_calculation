# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    POINTS = "Points"
    RECORDS = "Records"
    ACTIVITY = "Activity"
    ENTITIES = "Entities"
    ENTITIES_V2 = "Entities v2"
    RECENT_V2_ENTITIES_LIST = "Recent V2 Entities List"
    RELATED_ENTITIES = "Related Entities"
    ENTITY_CONNECTIONS = "Entity Connections"
    USER_PERMISSIONS = "User Permissions"
    USERS = "Users"
    NOTIFY = "Notify"
    ROLES = "Roles"
    PERMISSIONS = "Permissions"
    MODULES = "Modules"
