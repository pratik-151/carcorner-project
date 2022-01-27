from django.http import HttpResponse
from django.shortcuts import render
from pages.models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()
    context = {
        "teams": teams
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