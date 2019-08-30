from django import forms


class ContatoForm(forms.Form):
    email = forms.EmailField(required=True)
    assunto = forms.CharField(required=True)
    menssagem = forms.CharField(widget=forms.Textarea, required=True)