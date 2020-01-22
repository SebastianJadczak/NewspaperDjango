from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.template.loader import get_template
from django.views import View

from .forms import ContactForm, FormularzRejestracji
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import UserCreationForm

#Strona główna projektu
from .models import News


def index(request):
    news = News.objects.all()
    return render(request, 'index.html', {'news':news})

@login_required
def index_user(request):
    return render(request, 'index_user.html')

def test_response(request):
    return HttpResponse('test')

def wiadomosci(request):
    return HttpResponse('test-wiadomosci')

def sport(request):
    return HttpResponse('test')

def biznes(request):
    return HttpResponse('test')

def regionalne(request):
    return HttpResponse('test')

def kultura(request):
    return HttpResponse('test')

def styl_zycia(request):
    return HttpResponse('test')

def technologie(request):
    return HttpResponse('test')

def motoryzacja(request):
    return HttpResponse('test')



def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "kontakt.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')


class UserFormView(View):
    form_class = FormularzRejestracji
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('../index')

        return render(request, self.template_name, {'form': form})
