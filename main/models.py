from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        OWNER = "OWNER", "Owner"
        ASSOCIATION = "ASSOCIATION", "Association"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

#------------------------------------------------------------------

class OwnerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.OWNER)


class Owner(User):

    base_role = User.Role.OWNER

    Owner = OwnerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Owners"


@receiver(post_save, sender=Owner)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "OWNER":
        OwnerProfile.objects.create(user=instance)


class OwnerProfile(models.Model):
    # Need to change according to our requirements

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True)
    OwnerName=models.CharField(max_length=100, null=True)
    OwnerAddress = models.CharField(max_length=200, null=True)
    OwnerpNo = models.IntegerField( null=True)
    FlatNo = models.IntegerField( null=True)
    FloorNo = models.IntegerField( null=True)
#------------------------------------------------------------------

class AssociationManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ASSOCIATION)

class Association(User):

    base_role = User.Role.ASSOCIATION

    Association = AssociationManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for Association"


class AssociationProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True)
    AssociationName=models.CharField(max_length=100, null=True)
    AssociationAddress = models.CharField(max_length=200, null=True)
    AssociationRole = models.CharField(max_length=100)

@receiver(post_save, sender=Association)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "ASSOCIATION":
        AssociationProfile.objects.create(user=instance)