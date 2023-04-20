from django.http import JsonResponse
from connectedMail.models import ConnectedMail

def login_redirect(request):
    email = request.user.email
    
    if not ConnectedMail.objects.filter(mail = email).exists():
        new_connected_mail = ConnectedMail(mail = email)
        res = new_connected_mail.save()
        return JsonResponse({
            'status': 'create success',
            'response': res
        })
    return JsonResponse({
        'status': 'email already exist',
        'mail': email
    })