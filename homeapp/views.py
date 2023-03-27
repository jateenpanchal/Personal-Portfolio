from django.shortcuts import render,redirect

# Create your views here.

def homepage(request):
    return render(request,"homepage.html")

def resume(request):
    return render(request,"resume.html")

def project(request):
    return render(request,"project.html")

def contact(request):
    return render(request,"contact.html")

