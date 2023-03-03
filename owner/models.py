from django.db import models

# Create your models here.

class Notice(models.Model):
    notice_by = models.ForeignKey('main.Association', on_delete=models.CASCADE, null=True)
    notice_title = models.CharField(max_length=100, default="null")
    notice_desc = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.notice_title},"

