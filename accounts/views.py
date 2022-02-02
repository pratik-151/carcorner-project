from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST.get('password')
        print("username = ", username," type = ",type(username))
        print("password = ", password," type = ",type(password))
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Successfully Logged In')
            return redirect('dashboard')

        else:
            # Return an 'invalid login' error message.
            messages.error(request,'username or password does not match')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"email already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    auth.login(request,user)
                    messages.success(request,'You are logged in')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,"User successfully registered")
                    return redirect('login')
        else:
            messages.error(request,"password does not match")
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def logout_view(request):
    logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect('login')

def dashboard(request):
    return render(request,'accounts/dashboard.html')