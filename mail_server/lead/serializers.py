from rest_framework import serializers
from .models import Lead

class LeadModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        table_name = 'lead'
        fields = '__all__'