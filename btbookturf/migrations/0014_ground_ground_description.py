# Generated by Django 4.1.4 on 2023-04-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btbookturf', '0013_remove_booking_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='ground',
            name='ground_description',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]
