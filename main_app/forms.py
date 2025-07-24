from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Case

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Mate:
        modal = User
        fields = ['username', 'email',
                  'password1', 'password2']
        
class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'category']
        