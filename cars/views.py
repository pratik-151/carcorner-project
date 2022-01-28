from django.shortcuts import render
from cars.models import Car

# Create your views here.
def cars(request):
    cars = Car.objects.all().filter(is_featured=True)
    context = {
        'cars': cars
    }
    return render(request,'cars/cars.html',context=context)