# Generated by Django 4.1.4 on 2023-07-05 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btbookturf', '0028_alter_booking_user_pk'),
        ('members', '0006_remove_myusers_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusers',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='btbookturf.booking'),
        ),
    ]
