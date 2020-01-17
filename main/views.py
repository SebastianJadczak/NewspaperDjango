import send_email as send_email
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from main.models import News
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

theme = 'default'
data = {
    'lang':'pl',
    'charset' : 'utf-8',
    'title' : 'sproject.pl',
}



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

def kontakt(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            admin_addres = "S.Jadczak@il-pib.pl"
            responder_address = "responder@sproject.pl"
            client_address = form.email
            message_for_admin = """"
                    imię użytkownika: %s;
                    adres użytkownika: %s;
                    treść zapytania:
                        %s
                """ % (form.name, client_address, form.message)
            message_for_client = """
                    Witam,
                    dziękuję za wysłanie zapytania. Postaramy się na nie odpowiedzieć najszybciej jak się da
                           """
            try:
                send_email(form.subject, message_for_admin, responder_address, [admin_addres,])
                send_email(form.subject, message_for_client, responder_address, [client_address, ])
            except BadHeaderError:
                print("Wykryto niepoprawny naglowek")
            data['form'] = form
            data['info'] = 'dziękuje za wyslanie wiadomosci'
        else:
            form - ContactForm()
    return render(request, 'kontakt.html',data)

