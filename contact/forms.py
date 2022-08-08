from django import forms

class ContactoForm(forms.Form):
    name = forms.CharField(label="Nombre", required=False)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea())