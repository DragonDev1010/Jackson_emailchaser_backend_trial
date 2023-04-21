from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from user.models import User
from connectedMail.models import ConnectedMail
from .models import Campaign

client = Client()

class CampaignTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser', 
            email='testuser@example.com', 
            password='testpass'
        )

        self.connected_mail = ConnectedMail.objects.create(
            user_id=self.user.id,
            mail_provider_id=1, # assuming mail_provider with id=1 exists in the database
            email='testuser@example.com',
            access_token='testtoken',
            refresh_token='testrefresh'
        )

        self.campaign = Campaign.objects.create(
            sender_id=self.user.id,
            recipients=['recipient1@example.com', 'recipient2@example.com'],
            mail_subject='Test Campaign',
            mail_body='This is a test campaign.'
        )

    def test_create_new_campaign(self):
        url = reverse('create_new_campaign')
        data = {
            'sender_id': self.user.id,
            'recipients[]': ['recipient3@example.com', 'recipient4@example.com'],
            'mail_subject': 'New Campaign',
            'mail_body': 'This is a new campaign.'
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_start_campaign(self):
        url = reverse('start_campaign')
        data = {'campaign_id': self.campaign.id}
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
