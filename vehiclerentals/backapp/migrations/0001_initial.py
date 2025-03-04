# Generated by Django 4.1.4 on 2022-12-29 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarName', models.CharField(max_length=20)),
                ('Seats', models.IntegerField()),
                ('Large_bag', models.IntegerField()),
                ('Small_bag', models.IntegerField()),
                ('Mileage', models.CharField(max_length=20)),
                ('Price_For_3Days', models.IntegerField()),
                ('OwnerId', models.IntegerField()),
            ],
        ),
    ]
