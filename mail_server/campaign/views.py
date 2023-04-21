from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Campaign
from user.models import User
from connectedMail.models import ConnectedMail
from functions.gmail_with_oauth2 import send_gmail_with_oauth2
# Create your views here.
@api_view(['POST'])
def create_new_campaign(request):
    sender_id = request.POST.get('sender_id')
    
    if not User.objects.filter(id = sender_id).exists():
        return JsonResponse({
            'status': 'User does not exist'
        })
    
    recipients = request.POST.getList('recipients[]')
    mail_subject = request.POST.get('mail_subject')
    mail_body = request.POST.get('mail_body')
    schedule = request.POST.get('schedule')

    new_campaign = Campaign(
        sender_id = sender_id, 
        recipients = recipients, 
        mail_subject = mail_subject, 
        mail_body = mail_body
      )
    
    new_campaign.save()

def start_campaign(request):
    campaign_id = request.POST.get('campaign_id')

    if not Campaign.objects.filter(id = campaign_id).exists():
        return JsonResponse({
            'status': 'Campaign does not exist'
        })
    
    campaign = Campaign.objects.get(id = campaign_id)

    # get connected_email list from ConnectedMail model with user_id
    connected_mails = ConnectedMail.objects.all(user_id = campaign.sender_id)

    # check if connected mails list is not empty
    if connected_mails.count() == 0:
        return JsonResponse({'status': 'Does not exist connected mail'})
    
    for connected_mail in connected_mails:
        mail_provider_name = connected_mail.mail_provider.provider_name
        if mail_provider_name == 'gmail':
            send_gmail_with_oauth2(campaign.mail_subject, campaign.mail_body, connected_mail, request)
