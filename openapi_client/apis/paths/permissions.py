from openapi_client.paths.permissions.get import ApiForget
from openapi_client.paths.permissions.put import ApiForput
from openapi_client.paths.permissions.delete import ApiFordelete
from openapi_client.paths.permissions.patch import ApiForpatch


class Permissions(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
