# Generated by Django 3.2.12 on 2022-06-24 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0022_auto_20220624_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='short_description',
        ),
    ]
