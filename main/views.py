from msilib.schema import ListView

from django.contrib.admin.templatetags.admin_list import pagination
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm, FormularzRejestracji, FormSearch
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q

#Strona główna projektu
from .models import News, Product


def index(request):
    template_name = 'index.html'

    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query =request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True


    return render(request, 'index.html',{'form': form, 'news':news, 'list':list, 'flaga':flaga})







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


def zakupy(request):
    elements = Product.objects.all()
    return render(request, 'zakupy.html', {'elements':elements})


def search_results(request):
    return render(request, 'search_results.html')