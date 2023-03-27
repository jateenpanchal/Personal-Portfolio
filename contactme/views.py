from django.shortcuts import render,redirect
from .models import contactme
from .forms import contactmeform
from django.core.mail import  send_mail
# Create your views here.

def contact(request):
    data = contactmeform(request.POST)
    if request.method == "POST":
        if data.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            data.save()
            data = {
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'subject':subject,
                'message':message
            }
            message="""
            Firstname: {}
            Lastname: {}
            Subject: {}
            New Message:{}
            
            From: {}
            """.format( data['first_name'], data['last_name'],data['subject'],data['message'],data['email'])
            send_mail(data['subject'],message,"",['jateenp2002@gmail.com'])
            
            return redirect('contact')
        else:
            print('error')
    return render(request,'contact.html',{'data':data})

#  tdpejtupwlhhoohn