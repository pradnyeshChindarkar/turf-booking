# Generated by Django 4.1.4 on 2023-07-04 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btbookturf', '0017_booking_user_pk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='attendees',
        ),
        migrations.DeleteModel(
            name='MyUsers',
        ),
    ]
