from django.urls import path
from . import views
from .views import data

urlpatterns = [
    path('bha/',views.bha,name = 'bha'),
    path('tests/', views.tests,name = "tests"),
    path('html/',views.html,name = 'html'),
    path('data/',views.data,name ='data1')
    
]


