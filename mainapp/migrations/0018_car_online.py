# Generated by Django 3.2.9 on 2021-12-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20211206_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
