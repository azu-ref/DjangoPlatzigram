"""users forms"""

#django
from django import forms

#models
from django.contrib.auth.models import User
from users.models import Profile

class SignUpForm(forms.Form):
    """Sign Up Form"""

    CSS_HTML={
        'class': 'form-control',
        'required': True
    }

    username = forms.CharField(
        min_length=3, 
        max_length=10, 
        widget=forms.TextInput(attrs={**CSS_HTML, 'placeholder': 'Username'}))

    password = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput(attrs={**CSS_HTML, 'placeholder': 'Password'}))

    password_confirmation = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput(attrs={**CSS_HTML, 'placeholder': 'Password confirmation'}))

    first_name = forms.CharField(
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(attrs={**CSS_HTML, 'placeholder': 'First name'}))

    last_name = forms.CharField(
        min_length=2, 
        max_length=50,
        widget=forms.TextInput(attrs={**CSS_HTML, 'placeholder': 'Last name'}))

    email = forms.CharField(
        min_length=6, 
        max_length=70, 
        widget=forms.EmailInput(attrs={**CSS_HTML, 'placeholder': 'Email'}))

    def clean_username(self):
        """username most be unique"""
        username = self.cleaned_data['username']
        username_in_use = User.objects.filter(username=username).exists()
        if username_in_use:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match"""

        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match.')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
