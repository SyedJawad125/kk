from rest_framework.serializers import ModelSerializer
from utils.custom_exceptions import PasswordMustBeEightChar
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def validate(self,instance):
        if len(instance["password"]) < 7:
            raise PasswordMustBeEightChar()
        instance['password'] = make_password(instance['password'])
        return instance