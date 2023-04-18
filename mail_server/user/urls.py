from django.urls import path
from .views import users_list, create_new_user

urlpatterns = [
    path('', users_list, name='users_list'),
    path('create_new_user/', create_new_user, name='create_new_user')
]