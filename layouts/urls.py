from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home,name='home'),
    path('about',views.about,name='about'),
	path('contact', views.contact,name='contact'),
	path('services', views.services,name='services'),
	path('Content', views.Content,name='Content'),
    path('ProjectShow', views.ProjectShow,name='ProjectShow')
]