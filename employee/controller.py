from .serializers import UserSerializer
from utils.reusable import create_response, get_first_error_message
from utils.response_messages import *


class RegisterController:
    serializer_class = UserSerializer

    def create(self,request):
        try:
            serialized_data = self.serializer_class(data=request.data)

            if serialized_data.is_valid():
                instance = serialized_data.save()
                return create_response(self.serializer_class(instance).data, SUCCESSFUL, status_code=200)
            else:
                return create_response({}, get_first_error_message(serialized_data.errors, UNSUCCESSFUL), status_code=400)

        except Exception as e:
            return create_response({'error':str(e)}, SOMETHING_WENT_WRONG, 500)