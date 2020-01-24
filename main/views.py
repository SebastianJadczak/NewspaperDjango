from msilib.schema import ListView

from django.contrib.admin.templatetags.admin_list import pagination
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import ContactForm, FormularzRejestracji, FormSearch
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q

#Strona główna projektu
from .models import News, Product

class Index(View):

    form = FormSearch
    list = Product.objects.all()
    flaga = False
    news = News.objects.all()

    def get(self, request):
        template_name = 'index.html'
        query = request.GET.get('search')
        context = {'template_name':'index.html'}
        if query:
            self.list = self.list.filter(name=query)
            self.flaga = True
        return render(request, template_name, {'form': self.form, 'list': self.list, 'flaga': self.flaga,  'news': self.news,})



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
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def test_response(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def wiadomosci(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def sport(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def biznes(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def regionalne(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def kultura(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def styl_zycia(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def technologie(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})

def motoryzacja(request):
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})



def email(request):

    # wyszukiwarka
    form1 = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True

    #     Formularz kontaktowy
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
    return render(request, "kontakt.html", {'form': form,'form1': form1,  'list':list, 'flaga':flaga})

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
    news = News.objects.all()
    form = FormSearch
    list = Product.objects.all()
    flaga = False
    query = request.GET.get('search')
    if query:
        list = list.filter(name=query)
        flaga = True
    return render(request, 'index.html', {'form': form, 'news': news, 'list': list, 'flaga': flaga})


def search_results(request):
    return render(request, 'search_results.html')



