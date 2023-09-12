from django import forms

from .models import ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('first_name', 'last_name', 'email', 'password')
        labels = {
            "first_name": "",
            "last_name": "",
            "email": "",
            "password": "",
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password'}),
        }
