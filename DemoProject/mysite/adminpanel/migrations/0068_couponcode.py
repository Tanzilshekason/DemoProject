# Generated by Django 3.2.12 on 2022-07-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0067_remove_order_middlename'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('discount', models.IntegerField()),
            ],
        ),
    ]
