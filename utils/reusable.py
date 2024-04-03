from django.db import models
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def create_response(data, message, status_code):
    result = {
        "status_code": status_code,
        "message": message,
        "data": data
        }
    return Response(result, status=status_code)


def get_first_error_message(serialized_errors, default_message=""):
    if not serialized_errors:
        return default_message
    try:
        serialized_error_dict = serialized_errors
        if isinstance(serialized_errors, ReturnList):
            serialized_error_dict = serialized_errors[0]

        serialized_errors_keys = list(serialized_error_dict.keys())
        print(serialized_errors_keys)
        try:
            message = serialized_error_dict[serialized_errors_keys[0]][0].replace("This", serialized_errors_keys[0])
            print(message)
            return message
        except:
            return serialized_error_dict[serialized_errors_keys[0]][0]

    except Exception as e:
        return default_message