# Generated by Django 3.0.3 on 2020-12-28 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmsA', '0005_rating_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=10),
        ),
    ]
