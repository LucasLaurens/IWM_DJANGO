# Generated by Django 3.0.6 on 2020-05-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='clothes',
            field=models.ManyToManyField(to='shopping.Clothes'),
        ),
    ]
