# encryption/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.encryption_decryption_view, name='encrypt_decrypt'),
]
