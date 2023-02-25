from django.shortcuts import render,HttpResponse
# from .forms import Signup


# Create your views here.


def home(request):
    return render(request,'base/home.html')


def About(request):
    return render(request,'base/About.html')

def contact(request):
    return render(request,'base/contact.html')

def signup(request):
    # form = Signup()
    return render(request,'base/signup.html')

def login(request):
    return render(request,'base/login.html')