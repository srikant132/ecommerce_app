from django import forms
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()


#here we create Default djangoform for login

#Guest user
class GuestForm(forms.Form):
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm password' ,widget=forms.PasswordInput)

#this function is defined o confirm the password is matching or not
#here qs resposible for checking the existing username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("passwordmust match.")
        return data
