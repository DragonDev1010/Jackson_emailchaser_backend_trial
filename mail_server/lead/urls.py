from django.urls import path
from .views import show_list, create_new_lead

urlpatterns = [
    path('', show_list, name='show_list'),
    path('create_new_lead/', create_new_lead, name='create_new_lead')
]