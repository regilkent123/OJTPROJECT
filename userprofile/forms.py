from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile


class RegisterForm(forms.ModelForm):

    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def clean_username(self):
        # check if username data exists first before doing anything to it
        username_get = self.cleaned_data.get('username').lower()
        username_exist = User.objects.filter(username=username_get)
        if username_exist.exists():
            raise forms.ValidationError("Username already exists")
        return username_get

    def clean_email(self):
        # check if the email data is provided first before doing anything
        email_get = self.cleaned_data.get('email').lower()
        email_exist = User.objects.filter(email=email_get)
        if email_exist.exists():
            raise ValidationError("Email already exists")
        return email_get

    def clean_repassword(self):

        super(RegisterForm, self).clean()
        password_get = self.cleaned_data.get('password')
        repassword_get = self.cleaned_data.get('repassword')

        if password_get and repassword_get and password_get != repassword_get:
            raise ValidationError("Password don't match")

        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name')
        )
        return user


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['usertype', 'address', 'gender', 'height', 'weight']
        widgets = {
            'address': forms.Textarea(attrs={'cols': 10, 'rows': 20})
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = None
