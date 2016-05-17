from registration.forms import RegistrationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditProfileForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name', required=False)
    last_name = forms.CharField(label='Last Name', required=False)
    email = forms.EmailField(label='email', required=False)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
