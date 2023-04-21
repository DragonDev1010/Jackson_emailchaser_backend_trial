from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from user.models import User
from mailProvider.models import MailProvider
from .models import ConnectedMail
import json

class ConnectedMailTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.mail_provider = MailProvider.objects.create(provider_name='gmail', auth_endpoint='https://example.com', token_endpoint='https://example.com', client_id='client_id', client_secret='client_secret')
        self.connected_mail = ConnectedMail.objects.create(user=self.user, mail_address='test@example.com', mail_provider=self.mail_provider)

    def test_show_list(self):
        response = self.client.get(reverse('show_list'))
        connected_mails = ConnectedMail.objects.all()
        serialized_data = [{'id': str(cm.id), 'user': cm.user.id, 'mail_address': cm.mail_address, 'mail_provider': cm.mail_provider.id} for cm in connected_mails]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), serialized_data)

    def test_create_new_connected_mail(self):
        url = reverse('create_new_connected_mail')
        data = {
            'user_id': self.user.id,
            'mail_provider_id': self.mail_provider.id,
            'mail_address': 'newtest@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'status': 'success'})
        self.assertTrue(ConnectedMail.objects.filter(mail_address='newtest@example.com').exists())
