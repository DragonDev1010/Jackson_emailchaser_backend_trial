from django.urls import path
from .views import show_list

urlpatterns = [
    path('', show_list, name='show_list'),
    # path('create_new_user/', create_new_user, name='create_new_user')
]