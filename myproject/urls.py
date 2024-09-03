"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('property1', views.property1),
    path('form1', views.form1),
    path('quote', views.quote),
    path('thankyou', views.thankyou),
    path('subscription1', views.subscription1),
    path('propertytypes', views.propertytypes),
    path('subscription2', views.subscription2),
    path('subscription3', views.subscription3),
    path('form2', views.form2),
    path('form3', views.form3),
    path('commercial', views.commercial),
    path('flats', views.flats),
    path('houses', views.houses),
    path('plots', views.plots),
    path('villas', views.villas),
    path('about', views.about),
    path('contact', views.contact),
    path('login', views.user_login),  # Update this to match the renamed function
    path('registration', views.registration),
    path('logout/', views.custom_logout, name='logout'),  # Update this line
    path('saved_property/', views.saved_property),
]
