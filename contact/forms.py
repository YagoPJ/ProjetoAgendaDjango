from django.contrib.auth.models import User
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*'
            }
        )
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
        )

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True
    )
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe esse email cadastrado!', code='invalid')
            )
        return email