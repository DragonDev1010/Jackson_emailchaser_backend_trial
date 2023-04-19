from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Lead
from .serializers import LeadModelSerializer

# Create your views here.
def show_list(request):
    data = Lead.objects.all()
    serialized_data = LeadModelSerializer(data, many=True).data

    return JsonResponse(serialized_data, safe=False)

@api_view(['POST'])
def create_new_lead(request):
    serializer = LeadModelSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)