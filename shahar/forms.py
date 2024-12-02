from typing import Any
from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام کاربری خود را وارد کنید.'})

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'پسورد را وارد کنید.'})
        , max_length=20, required=True)
    

class RegisterForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام کاربری را وارد کنید'})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید.'})
        , required=False)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'پسورد خود را وارد کنید.'})
        , max_length=100, required=False)
        
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'پسورد خود را دوباره وارد کنید.'})
        , max_length=100, required=False)
    
    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirmPassword')
        if password != password2:
            raise forms.ValidationError('پسورد شما یکسان نیست.')
        
    def clean_userName(self):
        userName = self.cleaned_data.get('userName')
        query = User.objects.filter(username=userName)
        if query.exists():
            raise forms.ValidationError('این یوزر موجود است.')
        return userName

        