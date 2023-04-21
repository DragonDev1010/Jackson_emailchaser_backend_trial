from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import ConnectedMail
from user.models import User
from mailProvider.models import MailProvider
from .serializers import ConnectedMailModelSerializer

# Create your views here.
def show_list(request):
    data = ConnectedMail.objects.all()
    serialized_data = ConnectedMailModelSerializer(data, many=True).data

    return JsonResponse(serialized_data, safe=False)

@api_view(['POST'])
def create_new_connected_mail(request):
    user_id = request.POST.get('user_id')
    # check if there is User record with the `user_id`
    if not User.objects.filter(id = user_id).exists():
        return JsonResponse({'status': 'User does not exist.'})
    user = User.objects.get(id = user_id)

    mail_provider_id = request.POST.get('mail_provider_id')
    # check if there is MailProvider record with the `mail_provider_id`
    if not MailProvider.objects.filter(id = mail_provider_id).exists():
        return JsonResponse({'status': 'Mail Provider does not exist.'})
    mail_provider = MailProvider.objects.get(id = mail_provider_id)

    # mail = request.user.email
    mail_address = request.POST.get('mail_address')

    connected_mail = ConnectedMail(user = user, mail_address = mail_address, mail_provider = mail_provider)

    res = connected_mail.save()
    return JsonResponse({'status': 'success'})