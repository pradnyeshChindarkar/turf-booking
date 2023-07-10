# Generated by Django 4.1.4 on 2023-07-05 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('btbookturf', '0025_alter_booking_user_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user_pk',
            field=models.ForeignKey(blank=True, default='nul', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
