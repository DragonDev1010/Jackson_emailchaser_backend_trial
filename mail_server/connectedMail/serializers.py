from rest_framework import serializers
from .models import ConnectedMail
from user.models import User

class ConnectedMailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectedMail
        table_name = 'connected_mail'
        fields = '__all__'
    def create():
        return 1