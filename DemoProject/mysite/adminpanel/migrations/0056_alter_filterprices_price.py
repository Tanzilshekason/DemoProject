# Generated by Django 3.2.12 on 2022-07-07 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0055_auto_20220706_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterprices',
            name='price',
            field=models.CharField(max_length=60),
        ),
    ]
