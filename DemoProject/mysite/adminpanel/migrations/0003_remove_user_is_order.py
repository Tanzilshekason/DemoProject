# Generated by Django 3.2.12 on 2022-06-09 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_user_is_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_order',
        ),
    ]
