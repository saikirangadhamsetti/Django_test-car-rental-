# Generated by Django 4.1.4 on 2022-12-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rentlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerid', models.IntegerField()),
                ('owner_username', models.CharField(max_length=10)),
                ('customer_username', models.CharField(max_length=10)),
                ('Vehicleid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rentrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerid', models.IntegerField()),
                ('Vehicleid', models.IntegerField()),
                ('pickupdatetime', models.DateTimeField()),
                ('drop_offdatetime', models.DateTimeField()),
                ('status', models.CharField(choices=[('Accept', 'Accepted'), ('Reject', 'Rejected')], max_length=10)),
            ],
        ),
    ]
