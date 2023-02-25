from django.db import models

# Create your models here.
class Complaint(models.Model):
    complaint_desc = models.CharField(max_length=2000)
    issued_date = models.DateTimeField()
    resolved_date = models.DateTimeField(null=True)
