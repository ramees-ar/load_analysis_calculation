import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.points_api import PointsApi
from openapi_client.apis.tags.records_api import RecordsApi
from openapi_client.apis.tags.activity_api import ActivityApi
from openapi_client.apis.tags.entities_api import EntitiesApi
from openapi_client.apis.tags.entities_v2_api import EntitiesV2Api
from openapi_client.apis.tags.recent_v2_entities_list_api import RecentV2EntitiesListApi
from openapi_client.apis.tags.related_entities_api import RelatedEntitiesApi
from openapi_client.apis.tags.entity_connections_api import EntityConnectionsApi
from openapi_client.apis.tags.user_permissions_api import UserPermissionsApi
from openapi_client.apis.tags.users_api import UsersApi
from openapi_client.apis.tags.notify_api import NotifyApi
from openapi_client.apis.tags.roles_api import RolesApi
from openapi_client.apis.tags.permissions_api import PermissionsApi
from openapi_client.apis.tags.modules_api import ModulesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.POINTS: PointsApi,
        TagValues.RECORDS: RecordsApi,
        TagValues.ACTIVITY: ActivityApi,
        TagValues.ENTITIES: EntitiesApi,
        TagValues.ENTITIES_V2: EntitiesV2Api,
        TagValues.RECENT_V2_ENTITIES_LIST: RecentV2EntitiesListApi,
        TagValues.RELATED_ENTITIES: RelatedEntitiesApi,
        TagValues.ENTITY_CONNECTIONS: EntityConnectionsApi,
        TagValues.USER_PERMISSIONS: UserPermissionsApi,
        TagValues.USERS: UsersApi,
        TagValues.NOTIFY: NotifyApi,
        TagValues.ROLES: RolesApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.MODULES: ModulesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.POINTS: PointsApi,
        TagValues.RECORDS: RecordsApi,
        TagValues.ACTIVITY: ActivityApi,
        TagValues.ENTITIES: EntitiesApi,
        TagValues.ENTITIES_V2: EntitiesV2Api,
        TagValues.RECENT_V2_ENTITIES_LIST: RecentV2EntitiesListApi,
        TagValues.RELATED_ENTITIES: RelatedEntitiesApi,
        TagValues.ENTITY_CONNECTIONS: EntityConnectionsApi,
        TagValues.USER_PERMISSIONS: UserPermissionsApi,
        TagValues.USERS: UsersApi,
        TagValues.NOTIFY: NotifyApi,
        TagValues.ROLES: RolesApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.MODULES: ModulesApi,
    }
)
