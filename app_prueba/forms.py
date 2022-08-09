##app_prueba/forms.py
from django import forms

class RegistroForm(forms.Form):
    cliente_id = forms.CharField(label="cliente_id", required=True)
    email = forms.CharField(label="email", required=False)
    pwd = forms.CharField(label="pwd", required=False)



lista=[('0','Todos'),('3','Api'),  ('4','HomeBanking'), ('5', 'Movil')]
lista2=[('0','Todos'),('back','Back'),  ('front','Front'), ('ux', 'UX')]

class FiltroParticipantes(forms.Form):
    name = forms.CharField(label="Contiene:", required=False)
    #aca agregamos en el form, el campo de la fecha pero lo ocultamos en el template
    proyecto_id= forms.CharField(label='Que proyecto te intereso?', widget=forms.Select(choices=lista))
    team= forms.CharField(label='Que equipo te intereso?', widget=forms.Select(choices=lista2))