from django.db import models

# Create your models here.
class Complaint(models.Model):
    complaint_desc = models.CharField(max_length=2000)
    issued_date = models.DateTimeField()
    resolved_date = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f"{self.complaint_desc} - {self.issued_date}"

class Expenditure(models.Model):
    month = models.DateField()
    item = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.item} -> {self.amount}"
