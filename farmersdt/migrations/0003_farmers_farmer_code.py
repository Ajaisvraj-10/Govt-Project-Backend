# Generated by Django 4.2.4 on 2023-08-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmersdt', '0002_alter_aeo_fpo_alter_farmers_fpo_alter_farmers_ics_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmers',
            name='farmer_code',
            field=models.IntegerField(null=True),
        ),
    ]
