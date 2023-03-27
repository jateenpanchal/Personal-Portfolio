from django.contrib import admin
from django.urls import path
from contactme import urls
from . import views


urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("resume",views.resume,name="resume"),
    path("project",views.project,name="project"),
    path("contact",views.contact,name="contact"),
    # path("education",views.education,name="education"),
]
