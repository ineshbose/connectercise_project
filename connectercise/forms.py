from django import forms
from django.contrib.auth.models import User
from connectercise.models import SportRequest, Sport, UserProfile

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
    url = forms.URLField(max_length=200, help_text="Please enter the URL.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = SportRequest
        exclude = ('sport',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)