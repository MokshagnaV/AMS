from django.contrib import admin

# Register your models here.

from .models import Complaint, Expenditure

admin.site.register(Complaint)
admin.site.register(Expenditure)