# Generated by Django 3.2.9 on 2021-11-29 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20211129_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='filenames',
        ),
    ]