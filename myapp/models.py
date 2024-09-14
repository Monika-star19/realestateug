from django.db import models

class Sellerproperty(models.Model):
    owner_name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    property_type = models.CharField(max_length=100)
    bedrooms = models.CharField(max_length=2)
    bathrooms = models.CharField(max_length=2)
    floors = models.CharField(max_length=2)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=10)
    built = models.CharField(max_length=10)
    parking = models.CharField(max_length=5)
    ready = models.CharField(max_length=5)
    furnished = models.CharField(max_length=10)
    year = models.CharField(max_length=5)
    maintenance = models.CharField(max_length=200)
    money = models.CharField(max_length=20)
    hear = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return self.address

class Enquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    profession = models.CharField(max_length=100)
    rent_or_buy = models.CharField(max_length=10, choices=[('buy', 'Buy'), ('rent', 'Rent')])
    property_type = models.CharField(max_length=50, choices=[
        ('plots', 'Plots'),
        ('flats', 'Flats'),
        ('villas', 'Villas'),
        ('commercial_space', 'Commercial Space'),
        ('independent_house', 'Independent House')
    ])
    budget = models.CharField(max_length=50, choices=[
        ('10Lac-20Lac', '10Lac-20Lac'),
        ('30Lac-50Lac', '30Lac-50Lac'),
        ('50Lac-70Lac', '50Lac-70Lac'),
        ('70Lac-1Cr', '70Lac-1Cr'),
        ('1Cr+', '1Cr+')
    ])
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'