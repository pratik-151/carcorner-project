from django.http import HttpResponse
from django.shortcuts import render
from pages.models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    distinct_city = Car.objects.order_by('city').values_list('city', flat=True).distinct()
    distinct_model = Car.objects.order_by('model').values_list('model', flat=True).distinct()
    distinct_year = Car.objects.order_by('year').values_list('year', flat=True).distinct()
    distinct_body_style = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()
    context = {
        "teams": teams,
        'cars': cars,
        'distinct_city': distinct_city,
        'distinct_model': distinct_model,
        'distinct_year': distinct_year,
        'distinct_body_style':distinct_body_style,

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