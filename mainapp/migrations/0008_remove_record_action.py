# Generated by Django 3.2.9 on 2021-11-24 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20211124_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='action',
        ),
    ]
