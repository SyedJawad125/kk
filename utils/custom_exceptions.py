from rest_framework.exceptions import APIException
from rest_framework import status


class SessionExpired(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {'data': {}, 'message': 'Session Expired'}
    default_code = 'not_authenticated'


class PasswordMustBeEightChar(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {'data': {}, 'message': 'Password must be at least 8 characters long.'}
    default_code = 'not_authenticated'


class SameOldPassword(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = {'data': {}, 'message': 'New password cannot be same as old password'}
    default_code = 'not_authenticated'


class WrongOldPassword(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {'data': {}, 'message': 'Wrong Old Password'}
    default_code = 'not_authenticated'


class PasswordsDoesNotMatch(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {'data': {}, 'message': 'new_password and confirm_password are different'}
    default_code = 'not_authenticated'