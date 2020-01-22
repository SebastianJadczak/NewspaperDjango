from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)


class FormularzRejestracji(forms.ModelForm):
    username = forms.CharField(label="Login:", max_length=30)
    email = forms.EmailField(label="Email: ")
    password = forms.CharField(label='Hasło: ', widget=forms.PasswordInput())
    #password2 = forms.CharField(label='Hasło2: ', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
