# Generated by Django 3.2.12 on 2022-07-19 10:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0068_couponcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='couponcode',
            options={'verbose_name': 'Coupon Code', 'verbose_name_plural': 'Coupon Code'},
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.couponcode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='couponsused',
            name='coupon_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='coupon_id',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]