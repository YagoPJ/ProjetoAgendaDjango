from django.core.exceptions import ValidationError
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

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
    ...