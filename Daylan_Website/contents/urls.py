from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.resume, name='resume'),
    path('homepage/', views.homepage, name='homepage'),
]