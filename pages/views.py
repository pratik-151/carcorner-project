from django.http import HttpResponse
from django.shortcuts import render
from pages.models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    context = {
        "teams": teams,
        'cars': cars,
    }
    return render(request,'pages/home.html',context=context)

def about(request):
    teams = Team.objects.all()
    context = {
        "teams": teams
    }
    return render(request,"pages/about.html",context=context)

def contact(request):
    return render(request,"pages/contact.html")

def services(request):
    return render(request,"pages/services.html")