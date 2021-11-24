# Generated by Django 3.2.8 on 2021-10-22 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20211020_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='action',
            field=models.CharField(choices=[('MV', 'Movement'), ('LO', 'Loading'), ('UL', 'Unloading')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.car'),
        ),
        migrations.AddField(
            model_name='record',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.item'),
        ),
    ]