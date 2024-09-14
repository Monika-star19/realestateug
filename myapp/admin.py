from django.contrib import admin
from .models import Sellerproperty
from .models import Enquiry


# Register the Sellerproperty model
admin.site.register(Sellerproperty)
admin.site.register(Enquiry)

