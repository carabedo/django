from django import forms
import datetime

lista=[('3','Api'),  ('4','HomeBanking'), ('5', 'Movil')]


class ContactoForm(forms.Form):
    name = forms.CharField(label="Nombre", required=False)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea())
    date = forms.DateField(initial=datetime.date.today,widget = forms.HiddenInput())
    proyecto_id= forms.CharField(label='Que proyecto te intereso?', widget=forms.Select(choices=lista))

    