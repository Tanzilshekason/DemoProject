# Generated by Django 3.2.12 on 2022-07-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0057_auto_20220709_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(),
        ),
    ]
