from django.contrib import admin

# Register your models here.

from .models import Address

admin.site.register(Address)