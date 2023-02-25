from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app/home.html')


def explore(request):
    return render(request,'app/explore.html')

def notification(request):
    return render(request,'app/notification.html')

def profile(request):
    return render(request,'app/profile.html')