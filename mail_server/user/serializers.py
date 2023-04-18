from rest_framework import serializers
from user.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        table_name = 'user'
        fields = '__all__'