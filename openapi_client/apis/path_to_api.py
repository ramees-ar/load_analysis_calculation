import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.points import Points
from openapi_client.apis.paths.points_query import PointsQuery
from openapi_client.apis.paths.records_service import RecordsService
from openapi_client.apis.paths.records_service_record_id import RecordsServiceRecordId
from openapi_client.apis.paths.activity_measurement import ActivityMeasurement
from openapi_client.apis.paths.activity import Activity
from openapi_client.apis.paths.entities import Entities
from openapi_client.apis.paths.entities_entity_id import EntitiesEntityId
from openapi_client.apis.paths.entities_entity_id_connections import EntitiesEntityIdConnections
from openapi_client.apis.paths.entities_entity_id_connections_connection_id import EntitiesEntityIdConnectionsConnectionId
from openapi_client.apis.paths.graph_entities import GraphEntities
from openapi_client.apis.paths.graph_entities_entity_id import GraphEntitiesEntityId
from openapi_client.apis.paths.graph_entities_entity_id_list import GraphEntitiesEntityIdList
from openapi_client.apis.paths.graph_entities_relationship_info import GraphEntitiesRelationshipInfo
from openapi_client.apis.paths.users_user_id_role import UsersUserIdRole
from openapi_client.apis.paths.users_search import UsersSearch
from openapi_client.apis.paths.notify import Notify
from openapi_client.apis.paths.roles import Roles
from openapi_client.apis.paths.permissions import Permissions
from openapi_client.apis.paths.permissions_check import PermissionsCheck
from openapi_client.apis.paths.modules import Modules
from openapi_client.apis.paths.modules_module_id import ModulesModuleId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.POINTS: Points,
        PathValues.POINTS_QUERY: PointsQuery,
        PathValues.RECORDS_SERVICE: RecordsService,
        PathValues.RECORDS_SERVICE_RECORD_ID: RecordsServiceRecordId,
        PathValues.ACTIVITY_MEASUREMENT: ActivityMeasurement,
        PathValues.ACTIVITY: Activity,
        PathValues.ENTITIES: Entities,
        PathValues.ENTITIES_ENTITY_ID: EntitiesEntityId,
        PathValues.ENTITIES_ENTITY_ID_CONNECTIONS: EntitiesEntityIdConnections,
        PathValues.ENTITIES_ENTITY_ID_CONNECTIONS_CONNECTION_ID: EntitiesEntityIdConnectionsConnectionId,
        PathValues.GRAPH_ENTITIES: GraphEntities,
        PathValues.GRAPH_ENTITIES_ENTITY_ID: GraphEntitiesEntityId,
        PathValues.GRAPH_ENTITIES_ENTITY_ID_LIST: GraphEntitiesEntityIdList,
        PathValues.GRAPH_ENTITIES_RELATIONSHIP_INFO: GraphEntitiesRelationshipInfo,
        PathValues.USERS_USER_ID_ROLE: UsersUserIdRole,
        PathValues.USERS_SEARCH: UsersSearch,
        PathValues.NOTIFY: Notify,
        PathValues.ROLES: Roles,
        PathValues.PERMISSIONS: Permissions,
        PathValues.PERMISSIONS_CHECK: PermissionsCheck,
        PathValues.MODULES: Modules,
        PathValues.MODULES_MODULE_ID: ModulesModuleId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.POINTS: Points,
        PathValues.POINTS_QUERY: PointsQuery,
        PathValues.RECORDS_SERVICE: RecordsService,
        PathValues.RECORDS_SERVICE_RECORD_ID: RecordsServiceRecordId,
        PathValues.ACTIVITY_MEASUREMENT: ActivityMeasurement,
        PathValues.ACTIVITY: Activity,
        PathValues.ENTITIES: Entities,
        PathValues.ENTITIES_ENTITY_ID: EntitiesEntityId,
        PathValues.ENTITIES_ENTITY_ID_CONNECTIONS: EntitiesEntityIdConnections,
        PathValues.ENTITIES_ENTITY_ID_CONNECTIONS_CONNECTION_ID: EntitiesEntityIdConnectionsConnectionId,
        PathValues.GRAPH_ENTITIES: GraphEntities,
        PathValues.GRAPH_ENTITIES_ENTITY_ID: GraphEntitiesEntityId,
        PathValues.GRAPH_ENTITIES_ENTITY_ID_LIST: GraphEntitiesEntityIdList,
        PathValues.GRAPH_ENTITIES_RELATIONSHIP_INFO: GraphEntitiesRelationshipInfo,
        PathValues.USERS_USER_ID_ROLE: UsersUserIdRole,
        PathValues.USERS_SEARCH: UsersSearch,
        PathValues.NOTIFY: Notify,
        PathValues.ROLES: Roles,
        PathValues.PERMISSIONS: Permissions,
        PathValues.PERMISSIONS_CHECK: PermissionsCheck,
        PathValues.MODULES: Modules,
        PathValues.MODULES_MODULE_ID: ModulesModuleId,
    }
)
