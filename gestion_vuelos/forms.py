from django import forms

class FormularioContacto(forms.Form):
    asunto=forms.CharField(label="asunto", max_length=30, required=True)
    email=forms.EmailField(label="email", required=False)
    mensaje=forms.CharField(widget=forms.Textarea ,label="describe el asunto", max_length=300, required=True)