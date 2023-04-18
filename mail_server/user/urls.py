from django.urls import path
from .views import user_list, create_new_user

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create_new_user/', create_new_user, name='create_new_user')
]