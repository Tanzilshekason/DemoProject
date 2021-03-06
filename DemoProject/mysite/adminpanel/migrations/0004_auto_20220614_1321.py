# Generated by Django 3.2.12 on 2022-06-14 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_remove_user_is_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupons_used',
            options={'verbose_name': 'coupon_used', 'verbose_name_plural': 'coupon_used'},
        ),
        migrations.AlterModelOptions(
            name='product_images',
            options={'verbose_name': 'Product_images', 'verbose_name_plural': 'Product_images'},
        ),
        migrations.AlterField(
            model_name='banners',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(max_length=45, unique=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='modify_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='manage_user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product_images',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='created_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.category')),
            ],
        ),
    ]
