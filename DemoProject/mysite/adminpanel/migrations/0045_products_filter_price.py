# Generated by Django 3.2.12 on 2022-06-30 09:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0044_rename_filterprice_filterprices'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='filter_price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.filterprices'),
            preserve_default=False,
        ),
    ]