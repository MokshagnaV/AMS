# Generated by Django 4.1.5 on 2023-02-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_notices'),
    ]

    operations = [
        migrations.AddField(
            model_name='notices',
            name='notice_title',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
