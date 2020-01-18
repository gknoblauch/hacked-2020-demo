from django import forms

from buy_sell.models import Ad


class AdForm(forms.Form):

    title = forms.CharField(max_length=512)
    body = forms.CharField(widget=forms.Textarea)

    
