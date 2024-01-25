from django import forms

class ElectricityBillForm(forms.Form):
    consumo = forms.FloatField(required=False,initial=0)
    leitura_anterior = forms.FloatField(required=False,initial=0)
    leitura_atual = forms.FloatField(required=False,initial=0)