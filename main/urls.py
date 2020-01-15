from django.urls import path, include

from .views import test_response, index, index_user

urlpatterns = [
    path('test/', test_response),
    path('', index),
    path("index_user", index_user)
]