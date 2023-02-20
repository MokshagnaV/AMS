from django.contrib import admin

# Register your models here.
from .models import Owner, Notice

admin.site.register(Owner)
admin.site.register(Notice)