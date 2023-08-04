# Generated by Django 4.2.4 on 2023-08-04 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farmersdt', '0002_alter_aeo_fpo_alter_farmers_fpo_alter_farmers_ics_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countrty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Panchayats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('panchayat_code', models.IntegerField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panchayats_districts', to='locations.district')),
                ('fpo', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='panchayat_fpo', to='farmersdt.fpo')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_country', to='locations.countrty')),
            ],
        ),
        migrations.CreateModel(
            name='RevenueVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('panchayats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenuevillage_panchayats', to='locations.panchayats')),
            ],
        ),
        migrations.CreateModel(
            name='LocalVillage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('revenue_village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localvillage_revenuevillage', to='locations.revenuevillage')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_state', to='locations.state'),
        ),
    ]
