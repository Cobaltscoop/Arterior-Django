from django.contrib import admin
from django.db.models.lookups import In

# Register your models here.
from .models import Info

admin.site.register(Info)