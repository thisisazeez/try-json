from django.urls import path

from . import *
from . import views

urlpatterns = [
    path("",views.jsondata,name = "jsondata"),
]