# Generated by Django 3.1.6 on 2021-02-07 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
