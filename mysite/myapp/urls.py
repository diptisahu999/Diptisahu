from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('plogin',views.plogin,name='plogin'),
    path('DDocter',views.DDocter,name='DDocter'),
    path('PPatient',views.PPatient,name='PPatient'),
    path('PPregister',views.PPregister,name='PPregister'),
    path('potp/',views.potp,name='potp'),
    path('paymenthandler/',views.paymenthandler,name='paymenthandler'),



]