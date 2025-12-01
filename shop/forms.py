from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        label=_("نام"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        label=_("نام خانوادگی"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'})
    )
    email = forms.EmailField(
        max_length=254,
        label=_("ایمیل"),
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'})
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        label=_("نام کاربری"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'})
    )
    password1 = forms.CharField(
        label=_("رمز عبور"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'})
    )
    password2 = forms.CharField(
        label=_("تایید رمز عبور"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تایید رمز عبور'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        