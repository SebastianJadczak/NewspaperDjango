from django import forms
from django.contrib.auth.models import User

# Formularz kontaktowy
class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'email', }))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'subject', }))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'message', }))


# Formularz rejestracji do serwisu
class FormularzRejestracji(forms.ModelForm):
    username = forms.CharField(label="Login:", max_length=30, widget=forms.TextInput(attrs={'class': 'username_register first', }))
    email = forms.EmailField(label="Email: ",widget=forms.TextInput(attrs={'class': 'username_register'}))
    password = forms.CharField(label='Hasło: ', widget=forms.PasswordInput(attrs={'class': 'username_register'}))

    #Klasa dzięki czemu użytkownikom nie są dodawane 's' na końcu
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
