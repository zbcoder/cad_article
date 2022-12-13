from django.urls import path
from .views import *

urlpatterns = [
    path(r'start-page', start_page, name='start-page'),
    path(r'result-page', result, name='result-page')
]