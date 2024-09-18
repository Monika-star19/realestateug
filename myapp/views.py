from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Sellerproperty, Enquiry

# Create your views here.

def index(request):
    return render(request, 'index.html')

def property1(request):
    return render(request, 'property1.html')


def quote(request):
    return render(request, 'quote.html')

def success(request):
    return render(request, 'success.html')

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

def sellerform(request):
    return render(request,'sellerform.html')

def enquiry(request):
    return render(request,'enquiry.html')


def saveseller(request):
    if request.method == "POST":
        name = request.POST.get('owner-name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        property_type = request.POST.get('property-type')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        floors = request.POST.get('floors')
        address = request.POST.get('address')
        city = request.POST.get('city')
        area = request.POST.get('area')
        built = request.POST.get('built')
        parking = request.POST.get('parking')
        ready = request.POST.get('ready')
        furnished = request.POST.get('furnished')
        year = request.POST.get('year')
        maintenance = request.POST.get('maintenance')
        money = request.POST.get('money')
        hear = request.POST.get('hear')
        property_images = request.POST.get('property-images')
        property_video = request.POST.get('property-video')

        data = Sellerproperty(owner_name=name, number=number, email=email, property_type=property_type, bedrooms=bedrooms, bathrooms=bathrooms, floors=floors,
                              address=address, city=city, area=area, built=built, parking=parking, ready=ready, furnished=furnished, year=year, maintenance=maintenance,
                              money=money, hear=hear, image=property_images, video=property_video)

        data.save()

    return render(request,'success.html')


def enquirysave(request):
    if request.method == 'POST':
        first_name = request.POST.get('name')
        last_name = request.POST.get('last')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')
        profession = request.POST.get('profession')
        rent_or_buy = request.POST.get('rent/buy')
        property_type = request.POST.get('ready')
        budget = request.POST.get('budget')
        message = request.POST.get('message')

        # Create an instance of the Enquiry model with the form data
        data = Enquiry(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            profession=profession,
            rent_or_buy=rent_or_buy,
            property_type=property_type,
            budget=budget,
            message=message
        )

        # Save the instance to the database
        data.save()

        # Render the success page after saving
        return render(request, 'enquirysuccess.html')



def enquirysuccess(request):
    return render(request, 'enquirysuccess.html')

def properties(request):
    # Get query parameters from the URL
    location = request.GET.get('location')
    offer = request.GET.get('offer')
    property_type = request.GET.get('type')
    budget = request.GET.get('budget')

    # Add your filtering logic here, e.g., query the database based on these parameters

    # Pass the filtered data to the template
    return render(request, 'properties.html', {
        'location': location,
        'offer': offer,
        'property_type': property_type,
        'budget': budget,
    })


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')

def blogpage(request):
    return render(request, 'blogpage.html')

def blog1(request):
    return render(request, 'blog1.html')

def trends(request):
    return render(request, 'trends.html')


