from rest_framework.response import Response
from rest_framework.views import set_rollback
from rest_framework import status

class ApiException(Exception):
    status_code = status.HTTP_409_CONFLICT
    msg = "ApiException was raised!"
    additional_headers = {}


class ChildApiException(ApiException):
    status_code = status.HTTP_418_IM_A_TEAPOT
    msg = "ChildApiException was raised!"
    default_msg = "ChildApiException was raised!"


def api_exception_handler(exc, _):
    response_data = {
        "headers": getattr(exc, "additional_headers", {}),
        "data": {"msg": exc.msg},
        "status": exc.status_code,
    }
    set_rollback()
    return Response(**response_data)

def child_api_exception_handler(exc, _):
    response_data = {
        "headers": getattr(exc, "additional_headers", {}),
        "data": {"msg": exc.msg, "default_msg": exc.default_msg},
        "status": exc.status_code,
    }
    set_rollback()
    return Response(**response_data)