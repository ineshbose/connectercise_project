from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from connectercise.models import SportRequest, Sport, UserProfile, Comment
from location_field.forms.plain import PlainLocationField

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
    city = forms.CharField(max_length=255, help_text="Search Map", initial="Glasgow")
    location = PlainLocationField(based_fields=['city'], zoom=7, initial='55.87155490317328,-4.288530349731445', help_text="Move the pin around.")

    class Meta:
        model = SportRequest
        exclude = ('creator','slug','request_id','completed')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    field_order = ['sport','title', 'desc', 'views','suggested_date','city','location','picture']

class SportRequestForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    desc = forms.CharField(widget=forms.Textarea)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    suggested_date = forms.DateTimeField(widget=forms.SelectDateWidget(), required=False)
    city = forms.CharField(max_length=255, help_text="Search Map", initial="Glasgow")
    location = PlainLocationField(based_fields=['city'], zoom=7, initial='55.87155490317328,-4.288530349731445', help_text="Move the pin around.")

    class Meta:
        model = SportRequest
        exclude = ('creator','slug','sport','request_id','completed')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    field_order = ['title', 'desc', 'views','suggested_date','city','location','picture']


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
