# Generated by Django 4.1.4 on 2023-07-04 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('btbookturf', '0021_alter_booking_user_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user_pk',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.myusers'),
        ),
    ]