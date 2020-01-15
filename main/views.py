from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from main.models import News
# Create your views here.

#Strona główna projektu

def index(request):
    news = News.objects.all()
    return render(request, 'index.html')

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



