from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.

def index(request):
    return render(request, 'index.html')

def property1(request):
    return render(request, 'property1.html')


def quote(request):
    return render(request, 'quote.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def subscription1(request):
    return render(request, 'subscription1.html')

def propertytypes(request):
    return render(request, 'propertytypes.html')

def subscription2(request):
    return render(request, 'subscription2.html')

def subscription3(request):
    return render(request, 'subscription3.html')

def commercial(request):
    return render(request, 'commercial.html')

def flats(request):
    return render(request, 'flats.html')

def houses(request):
    return render(request, 'houses.html')

def plots(request):
    return render(request, 'plots.html')

def villas(request):
    return render(request, 'villas.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use Django's built-in login function
            return redirect('/')
        else:
            return redirect('/login')

    return render(request, 'login.html')
def registration(request):

    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('/')

    return render(request, 'registration.html')

def custom_logout(request):
    auth_logout(request)
    return render(request, 'index.html')

def properties(request):
    return render(request, 'properties.html')






