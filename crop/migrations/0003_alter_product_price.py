# Generated by Django 4.2.4 on 2023-08-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]