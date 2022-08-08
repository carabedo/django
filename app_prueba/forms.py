##app_prueba/forms.py
from django import forms

class RegistroForm(forms.Form):
    cliente_id = forms.CharField(label="cliente_id", required=True)
    email = forms.CharField(label="email", required=False)
    pwd = forms.CharField(label="pwd", required=False)