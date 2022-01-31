from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cars.models import Car

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    distinct_city = Car.objects.order_by('city').values_list('city', flat=True).distinct()
    distinct_model = Car.objects.order_by('model').values_list('model', flat=True).distinct()
    distinct_year = Car.objects.order_by('year').values_list('year', flat=True).distinct()
    distinct_body_style = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()

    paginator = Paginator(cars,2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    context = {
        'cars': paged_cars,
        'distinct_city': distinct_city,
        'distinct_model': distinct_model,
        'distinct_year': distinct_year,
        'distinct_body_style':distinct_body_style,
    }
    return render(request,'cars/cars.html',context=context)

def car_details(request,id):
    car = get_object_or_404(Car,pk=id)
    # print("car= ",car.car_title)
    context = {
        'car': car
    }
    return render(request,'cars/car-details.html',context=context)

def search(request):
    cars = Car.objects.order_by('-created_date').filter(is_featured=True)

    distinct_city = Car.objects.order_by('city').values_list('city', flat=True).distinct()
    distinct_model = Car.objects.order_by('model').values_list('model', flat=True).distinct()
    distinct_year = Car.objects.order_by('year').values_list('year', flat=True).distinct()
    distinct_body_style = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()
    distinct_transmission = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if min_price and max_price:
            cars = cars.filter(price__range=(min_price,max_price))


    context = {
        'cars': cars,
        'distinct_city': distinct_city,
        'distinct_model': distinct_model,
        'distinct_year': distinct_year,
        'distinct_body_style':distinct_body_style,
        'distinct_transmission':distinct_transmission
    }
    # for car in cars:
    #     print("car= ",car)
    
    return render(request,'cars/search.html',context=context)
