from django import forms
from.models import Passwords

class ProductForm(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ['website', 'username', 'password']