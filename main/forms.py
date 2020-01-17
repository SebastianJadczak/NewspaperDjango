from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(label="name@domain.com")
    subject = forms.CharField(max_length=70)
    message = forms.CharField(widget=forms.Textarea)

