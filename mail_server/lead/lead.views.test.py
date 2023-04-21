from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Lead
from .serializers import LeadModelSerializer
import json

# initialize the APIClient app
client = Client()

class LeadListCreateViewTestCase(TestCase):
    def setUp(self):
        self.valid_payload = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'phone': '1234567890',
            'message': 'Hello, I am interested in your product.'
        }
        self.invalid_payload = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalidemail',
            'phone': '1234567890',
            'message': 'Hello, I am interested in your product.'
        }
        Lead.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.com',
            phone='0987654321',
            message='Hello, I am interested in your product.'
        )

    def test_show_list(self):
        # get API response
        response = client.get(reverse('lead_list'))
        # get data from db
        leads = Lead.objects.all()
        serializer = LeadModelSerializer(leads, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_lead_valid_payload(self):
        response = client.post(
            reverse('lead_create'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_new_lead_invalid_payload(self):
        response = client.post(
            reverse('lead_create'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
