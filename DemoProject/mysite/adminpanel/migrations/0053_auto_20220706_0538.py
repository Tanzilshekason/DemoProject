# Generated by Django 3.2.12 on 2022-07-06 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0052_alter_images_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='couponsused',
            options={'verbose_name': 'coupon used', 'verbose_name_plural': 'coupon used'},
        ),
        migrations.AlterModelOptions(
            name='userorder',
            options={'verbose_name': 'user order', 'verbose_name_plural': 'user order'},
        ),
    ]
