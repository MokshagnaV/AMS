# Generated by Django 4.1.5 on 2023-03-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0004_complaint_complaint_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]