from django.contrib import admin

# Register your models here.

from .models import Owner, OwnerProfile, Association, AssociationProfile, User

admin.site.register(Owner)
admin.site.register(OwnerProfile)
admin.site.register(Association)
admin.site.register(AssociationProfile)
admin.site.register(User)


