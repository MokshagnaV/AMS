from django.db import models

# Create your models here.

class Owner(models.Model):
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    floor_no = models.IntegerField()
    flat_no = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name},{self.flat_no}"
    
class Notice(models.Model):
    notice_title = models.CharField(max_length=100, default="null")
    notice_desc = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.notice_title},"
