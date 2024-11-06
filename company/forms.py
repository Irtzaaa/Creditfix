# company/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company

class CompanyRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'
        })
    )
    company_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'
        })
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'company_name', 'address', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border rounded focus:outline-none focus:ring focus:border-blue-300'
        })
