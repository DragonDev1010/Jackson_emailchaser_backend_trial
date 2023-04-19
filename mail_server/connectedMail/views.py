from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import ConnectedMail
from user.models import User
from .serializers import ConnectedMailModelSerializer

# Create your views here.
def show_list(request):
    data = ConnectedMail.objects.all()
    serialized_data = ConnectedMailModelSerializer(data, many=True).data

    return JsonResponse(serialized_data, safe=False)

@api_view(['POST'])
def create_new_connected_mail(request):
    user_id = request.POST.get('user_id')
    mail = request.POST.get('mail')

    user = User.objects.get(id = user_id)

    connected_mail = ConnectedMail(user = user, mail = mail)

    res = connected_mail.save()
    return JsonResponse({'status': 'success'})