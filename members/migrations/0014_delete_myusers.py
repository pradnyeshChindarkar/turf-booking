# Generated by Django 4.1.4 on 2023-07-05 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_alter_myusers_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyUsers',
        ),
    ]
