from django import forms

class RegistrationForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder':"Subject"}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control"}))