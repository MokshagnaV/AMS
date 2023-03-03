# Generated by Django 4.1.5 on 2023-03-02 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_associationprofile_user_and_more'),
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_desc', models.CharField(max_length=500)),
                ('payment_mode', models.CharField(max_length=100)),
                ('UTR', models.CharField(max_length=100)),
                ('payment_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.owner')),
            ],
        ),
    ]