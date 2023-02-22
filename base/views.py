from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return render(request,'base/home.html')


def About(request):
    return render(request,'base/About.html')

def contact(request):
    return render(request,'base/contact.html')


