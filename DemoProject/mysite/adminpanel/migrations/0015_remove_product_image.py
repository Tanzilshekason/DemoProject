# Generated by Django 3.2.12 on 2022-06-24 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0014_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
