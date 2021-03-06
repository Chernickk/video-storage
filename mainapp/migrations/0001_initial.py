# Generated by Django 3.2.8 on 2021-10-18 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.car')),
            ],
            options={
                'db_table': 'record',
            },
        ),
    ]
