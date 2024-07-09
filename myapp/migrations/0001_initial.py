# Generated by Django 5.0.6 on 2024-07-09 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('bike_id', models.AutoField(primary_key=True, serialize=False)),
                ('bike_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('rental_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.bike')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.rental')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]