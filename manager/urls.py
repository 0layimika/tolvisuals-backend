from django.urls import path
from .views import *

urlpatterns=[
    path('client-manager/login',login, name='login'),
    path('',home, name='home'),
    path('client-manager/create-client',create_client, name='create-client'),
    path('client-manager/client/<int:id>', client_details, name="client-details"),
    path('client-manager/add-images/<int:id>', add_images, name='add-images'),
    path('client-manager/delete-images/<int:id>',delete_images,name='delete-images'),
    path('client-manager/delete-client/<int:id>',delete_client, name='delete-client')
]