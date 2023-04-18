from django.shortcuts import render
from django.http import JsonResponse
from .models import User

# Create your views here.
def user_list(request):
    # users = User.objects.all()
    data = {'message': 'Hello, world!'}
    return JsonResponse(data)