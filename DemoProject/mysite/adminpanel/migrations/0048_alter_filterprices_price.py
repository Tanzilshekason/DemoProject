# Generated by Django 3.2.12 on 2022-06-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0047_products_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterprices',
            name='price',
            field=models.CharField(choices=[('100 TO 199', '100 TO 199'), ('200 TO 299', '200 TO 299'), ('300 TO 399', '300 TO 399'), ('400 TO 499', '400 TO 499'), ('500 TO 600', '500 TO 600')], max_length=60),
        ),
    ]
