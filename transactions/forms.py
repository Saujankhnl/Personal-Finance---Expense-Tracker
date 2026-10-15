from django import forms
from django.contrib.auth.forms import AuthenticationForm

class RememberMeAuthForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=True)