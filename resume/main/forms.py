from django import forms
from .models import UserDetails,Experience,Projects,Education 

class ResumeDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['first_name','last_name','phone','user','email','interests','img','address'] 

class ExperienceForm(forms.ModelForm):
    class Meta:
        model=Experience
        fields=['title', 'companyName', 'data', 'date', 'user']

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields=['collegeName', 'date', 'Degree', 'user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Projects        
        fields=['heading', 'img', 'desc', 'user']