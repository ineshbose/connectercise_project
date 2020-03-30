from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from connectercise.models import SportRequest, Sport, UserProfile, Comment

class SportForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the sport name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Sport
        fields = ('name',)

class RequestForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    desc = forms.CharField(widget=forms.Textarea)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    suggested_date = forms.DateTimeField(widget=forms.SelectDateWidget(), required=False)

    class Meta:
        model = SportRequest
        exclude = ('creator','slug','request_id','completed')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

class SportRequestForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    desc = forms.CharField(widget=forms.Textarea)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    suggested_date = forms.DateTimeField(widget=forms.SelectDateWidget(), required=False)


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

class UserForm2(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','first_name','last_name')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
