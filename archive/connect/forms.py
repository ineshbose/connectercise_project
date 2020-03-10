from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from connect.models import UserProfile

class SignUpForm(UserCreationForm):
    dateOfBirth = forms.DateField(help_text='Format: YYYY-MM-DD', label='Date of Birth')
    profilePhoto = forms.ImageField(label='Profile Photo')
    sex = forms.ChoiceField(choices=UserProfile.SEX)
    sport_lookingFor = forms.ChoiceField(choices=UserProfile.sport_choices, label='Sport')

    class Meta:
        model = User
        fields = ('username',
                    'first_name', 
                    'last_name', 
                    'email', 
                    'dateOfBirth', 
                    'sex', 
                    'lookingFor',
                    'profilePhoto', 
                    'password1', 
                    'password2')

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='')