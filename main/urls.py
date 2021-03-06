from django.urls import path
from django.conf.urls import url

from . import views
from .views import test_response, index, index_user, wiadomosci, sport, biznes, regionalne, kultura, styl_zycia, \
    technologie, motoryzacja, email, UserFormView, zakupy, search_results

urlpatterns = [
    path('test/', test_response),
    path('', views.Index.as_view(), name='index'),
    path("index_user", index_user),
    path('wiadomosci', wiadomosci, name='wiadomosci'),
    path('sport', sport, name='sport'),
    path('biznes', biznes, name='biznes'),
    path('regionalne', regionalne, name='regionalne'),
    path('kultura', kultura, name='kultura'),
    path('styl_zycia', styl_zycia, name='styl_zycia'),
    path('technologie', technologie, name='technologie'),
    path('motoryzacja', motoryzacja, name='motoryzacja'),
    path('kontakt', email, name='kontakt'),
    path('zakupy', zakupy, name='zakupy'),
    url(r'^search_results^$', search_results, name='search_results'),
    path('register/', views.UserFormView.as_view(), name='register'),
    url(r'^register^$', views.UserFormView.as_view(), name='register'),
    url(r'^email/$',
        views.email,
        name='email'
        ),
    url(r'^thanks/$',
        views.thanks,
        name='thanks'
        ),

]


