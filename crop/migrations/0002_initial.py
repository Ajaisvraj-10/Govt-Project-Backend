# Generated by Django 4.2.4 on 2023-08-09 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmersdt', '0001_initial'),
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropsinfarmer',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cropsinfarmer_farmer', to='farmersdt.farmers'),
        ),
        migrations.AddField(
            model_name='cropsinfarmer',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cropsinfarmer_plant', to='crop.plant'),
        ),
    ]
