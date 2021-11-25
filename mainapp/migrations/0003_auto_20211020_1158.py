# Generated by Django 3.2.8 on 2021-10-20 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_record_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='car',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='mainapp.car'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('datetime', models.DateTimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.car')),
            ],
            options={
                'db_table': 'gps',
            },
        ),
    ]
