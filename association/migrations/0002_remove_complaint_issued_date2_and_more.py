# Generated by Django 4.1.5 on 2023-02-21 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='issued_date2',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='resolved_date',
            field=models.CharField(default='Not Yet Resolved', max_length=20),
        ),
    ]
