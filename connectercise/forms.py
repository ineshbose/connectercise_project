from django import forms
from django.contrib.auth.models import User
from connectercise.models import SportRequest, Sport, UserProfile, Comment

class SportForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the sport name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Sport
        fields = ('name',)

class RequestForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title.")
    desc = forms.CharField(help_text="Please enter a description.", widget=forms.Textarea)
    #suggested_time = forms.DateTimeField(help_text="Enter a suggested time (optional).", required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = SportRequest
        exclude = ('creator','slug','request_id','completed')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

class SportRequestForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title.")
    desc = forms.CharField(help_text="Please enter a description.", widget=forms.Textarea)
    #suggested_time = forms.DateTimeField(help_text="Enter a suggested time (optional).", required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = SportRequest
        exclude = ('creator','slug','sport','request_id','completed')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, help_text="First Name")
    last_name = forms.CharField(max_length=128, help_text="Last Name")

    class Meta:
        model = UserProfile
        fields = ('picture',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')