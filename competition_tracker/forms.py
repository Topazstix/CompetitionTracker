from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Competition, ClubMember

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'description', 'start_date', 'end_date', 'club_member']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        help_texts = {
            'name': 'Enter the name of the competition.',
            'description': 'Enter a detailed description of the competition.',
        }

class ClubMemberForm(forms.ModelForm):
    class Meta:
        model = ClubMember
        fields = ['name', 'username', 'email']
        help_texts = {
            'name': 'Enter the full name of the club member.',
            'username': 'Enter the preferred username for the club member.',
            'email': 'Enter the email address of the club member.',
        }


## User registration form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': 'Enter a username for the new user.',
            'email': 'Enter the email address of the new user.',
            'password1': 'Enter a password for the new user.',
            'password2': 'Confirm the password for the new user.',
        }