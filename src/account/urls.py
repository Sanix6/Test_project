from django.urls import path
from .views import *


urlpatterns = [
    path('login/', ModelListView.as_view(), name='login')
]

