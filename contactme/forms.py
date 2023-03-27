from django import forms
from .models import contactme

class contactmeform(forms.ModelForm):
    class Meta:
        model = contactme
        fields = ("__all__")
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your First Name"})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Last Name"})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Email"})
        self.fields['subject'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Subject"})
        self.fields['message'].widget.attrs.update({'class':'form-control','placeholder':"Enter Your Message"})
