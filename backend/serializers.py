from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'father_name', 'grandfather_name',
                 'email', 'phone_number', 'password', 'registration_date' )