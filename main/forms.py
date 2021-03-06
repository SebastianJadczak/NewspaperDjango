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


#Formularz dodawania produktów do koszyka

class FormsAddProducts(forms.Form):
    name = forms.CharField(max_length=120)
    description = forms.CharField(max_length=600, widget=forms.Textarea(attrs={'class': 'description_product'}))
    photo = forms.ImageField()
    price = forms.FloatField(required=False, max_value=999999, min_value=0,)

class FormSearch(forms.Form):

    search = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={'name': 'search'}))