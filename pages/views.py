from django.http import HttpResponse
from django.shortcuts import redirect, render
from pages.models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

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
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        email_message = f'Full name: {fullname}\nEmail: {email}\nphone: {phone}\nMessage: {message}'

        admin_email = User.objects.get(is_superuser=True).email

        send_mail(
        subject,
        email_message,
        'from@example.com', # i don't want email to be publish
        [admin_email],
        fail_silently=False,
        )

        messages.success(request,'Successfully submitted message, We will contact you soon.')
        return redirect('contact')
        
    return render(request,"pages/contact.html")

def services(request):
    return render(request,"pages/services.html")