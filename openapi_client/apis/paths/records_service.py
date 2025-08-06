from openapi_client.paths.records_service.get import ApiForget
from openapi_client.paths.records_service.put import ApiForput
from openapi_client.paths.records_service.post import ApiForpost
from openapi_client.paths.records_service.delete import ApiFordelete
from openapi_client.paths.records_service.patch import ApiForpatch


class RecordsService(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
