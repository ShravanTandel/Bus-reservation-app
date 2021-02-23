# Generated by Django 3.0.3 on 2020-12-30 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busno', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('departuretime', models.TimeField(max_length=10)),
                ('date', models.DateField()),
                ('bustype', models.CharField(choices=[('AC', 'AC'), ('NON AC', 'NON AC')], max_length=10)),
                ('duration', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('rate', models.FloatField(default=5.0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('registereddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=10)),
                ('date', models.DateField()),
                ('age', models.IntegerField()),
                ('emailid', models.EmailField(max_length=254)),
                ('phoneno', models.CharField(max_length=20)),
                ('busno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmsA.BusInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatno', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('busno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmsA.BusInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('experience', models.TextField(null=True)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmsA.BusInfo')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmsA.Passenger')),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='seatno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmsA.Seats'),
        ),
        migrations.AddField(
            model_name='passenger',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passenger', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='businfo',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbmsA.Company'),
        ),
    ]
