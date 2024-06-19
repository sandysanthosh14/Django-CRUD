from django import forms
from myapp.models import Student

# Create your models here.
class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    
