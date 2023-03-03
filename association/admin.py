from django.contrib import admin

# Register your models here.

from .models import Complaint, Expenditure, Payment, BankBalance

admin.site.register(Complaint)
admin.site.register(Expenditure)
admin.site.register(Payment)
admin.site.register(BankBalance)