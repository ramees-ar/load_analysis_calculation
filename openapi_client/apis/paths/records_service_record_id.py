from openapi_client.paths.records_service_record_id.get import ApiForget
from openapi_client.paths.records_service_record_id.put import ApiForput
from openapi_client.paths.records_service_record_id.delete import ApiFordelete
from openapi_client.paths.records_service_record_id.patch import ApiForpatch


class RecordsServiceRecordId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
