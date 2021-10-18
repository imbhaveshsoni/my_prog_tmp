from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('sign_up', views.sign_up,name='sign_up'),
    path('sign_in', views.sign_in,name='sign_in'),
    path('sign_out', views.sign_out,name='sign_out'),
    path('dashboard', views.dashboard,name='dashboard'),
]