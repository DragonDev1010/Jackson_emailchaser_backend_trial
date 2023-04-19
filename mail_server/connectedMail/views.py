from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import ConnectedMail
from .serializers import ConnectedMailModelSerializer

# Create your views here.
def show_list(request):
    data = ConnectedMail.objects.all()
    serialized_data = ConnectedMailModelSerializer(data, many=True).data

    return JsonResponse(serialized_data, safe=False)
