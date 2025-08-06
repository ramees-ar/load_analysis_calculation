from openapi_client.paths.graph_entities_entity_id.get import ApiForget
from openapi_client.paths.graph_entities_entity_id.put import ApiForput
from openapi_client.paths.graph_entities_entity_id.delete import ApiFordelete
from openapi_client.paths.graph_entities_entity_id.patch import ApiForpatch


class GraphEntitiesEntityId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
