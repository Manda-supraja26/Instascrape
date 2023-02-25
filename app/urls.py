from django.urls import path
from . import views
app_name= 'app'
urlpatterns= [
    path("home/",views.home,name= "home"),
    path("explore/",views.explore,name="explore"),
    path("notification/",views.notification,name="notification"),
    path("profile/",views.profile,name="profile")

]