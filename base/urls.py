from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.About,name="about"),
    path('contact/',views.contact,name="contact")
    
]
