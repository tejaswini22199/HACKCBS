# Generated by Django 3.1.3 on 2020-11-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20201108_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproduct',
            name='phonenumber',
            field=models.TextField(max_length=20),
        ),
    ]