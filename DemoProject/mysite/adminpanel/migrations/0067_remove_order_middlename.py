# Generated by Django 3.2.12 on 2022-07-15 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0066_auto_20220714_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='middlename',
        ),
    ]