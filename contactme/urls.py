from django.contrib import admin
from django.urls import path
from contactme import urls
from . import views


urlpatterns = [
    path("",views.contact,name="contact"),
]
