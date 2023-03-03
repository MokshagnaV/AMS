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
    PAYMENT_FOR_CHOICE = (
        ('MB', 'Maintenance Bill'),
        ('FH', 'Function Hall'),
        ('OB', 'Other Bill')
    )

    user = models.ForeignKey('main.Owner', on_delete=models.CASCADE)
    payment_for = models.CharField(max_length=2, choices=PAYMENT_FOR_CHOICE, null=True)
    payment_desc = models.CharField(max_length=500)
    payment_mode = models.CharField(max_length = 100)
    reciept_no = models.CharField(max_length=10, null = True)
    UTR = models.CharField(max_length=100, null=True)
    payment_date = models.DateField()
    amount = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user}, {self.payment_mode}"

class BankBalance(models.Model):
    month = models.DateField()
    balance = models.IntegerField()

    def __str__(self):
        return f"{self.month.month} -> {self.balance}"