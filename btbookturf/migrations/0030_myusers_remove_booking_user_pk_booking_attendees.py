# Generated by Django 4.1.4 on 2023-07-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btbookturf', '0029_alter_booking_user_pk'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_user', models.CharField(default=1, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='User Mail')),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_pk',
        ),
        migrations.AddField(
            model_name='booking',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='btbookturf.myusers'),
        ),
    ]
