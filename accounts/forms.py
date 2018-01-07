from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    confirmpassword = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_confirmpassword(self):
        password = self.cleaned_data.get('password')
        confirmpassword = self.cleaned_data.get('confirmpassword')

        if password and confirmpassword and password != confirmpassword:
            raise ValidationError("Password's do not match")

        return confirmpassword

<<<<<<< HEAD
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        r = User.objects.filter(first_name=first_name)
        if r.count():
            raise  ValidationError("Username already exists")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        r = User.objects.filter(last_name=last_name)
        if r.count():
            raise  ValidationError("Username already exists")
        return first_name

=======
>>>>>>> 96c979f4222ce75b09611ebba7afe828e513e75d
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password']
        )
        if commit:
            user.save()
        return user
