from django.db import models

# Create your models here.
class Complaint(models.Model):
    complaint_by = models.ForeignKey('main.Owner', on_delete=models.CASCADE, null=True)
    complaint_desc = models.CharField(max_length=2000)
    issued_date = models.DateTimeField()
    resolved_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.complaint_desc} - {self.issued_date}"

class Expenditure(models.Model):
    month = models.DateField()
    item = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.item} -> {self.amount}"

class Payment(models.Model):
    user = models.ForeignKey('main.Owner', on_delete=models.CASCADE)
    payment_desc = models.CharField(max_length=500)
    payment_mode = models.CharField(max_length = 100)
    UTR = models.CharField(max_length=100, null=True)
    payment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user}, {self.payment_mode}"