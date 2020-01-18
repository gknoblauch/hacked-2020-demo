from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from buy_sell.models import Ad, LANGUAGES


class AdForm(forms.Form):

    title = forms.CharField(max_length=512)
    body = forms.CharField(widget=forms.Textarea)


class SignUpForm(UserCreationForm):
    preferred_language = forms.ChoiceField(choices=LANGUAGES, initial="en")
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'preferred_language')


    
