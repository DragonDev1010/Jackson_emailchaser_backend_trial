from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserModelSerializer

# Create your views here.
@api_view(['POST'])
def create_new_user(request):
  serializer = UserModelSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
    return JsonResponse(serializer.data, status=201)
  return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_list(request):
  return JsonResponse({'status': 'GET success'})