from django.urls import path
from .views import show_list, create_new_connected_mail

urlpatterns = [
    path('', show_list, name='show_list'),
    path('create_new_connected_mail/', create_new_connected_mail, name='create_new_connected_mail')
]