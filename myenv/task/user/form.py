from .models import MyModel
from django import forms


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["name", "email", "phonenumber", "password"]
