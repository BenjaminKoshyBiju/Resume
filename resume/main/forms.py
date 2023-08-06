from django import forms
from .models import UserDetails 

class ResumeDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['first_name','last_name','phone','user','email','interests','img','address'] 