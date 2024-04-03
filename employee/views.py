from rest_framework.viewsets import ModelViewSet
from .controller import *


register_controller = RegisterController()

class RegisterAPIView(ModelViewSet):
    def create(self,request):
        return register_controller.create(request)