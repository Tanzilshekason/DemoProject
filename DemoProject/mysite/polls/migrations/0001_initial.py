# Generated by Django 3.2.12 on 2022-06-03 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_path', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent_id', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='cms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('meta_title', models.TextField()),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.TextField()),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conf_key', models.CharField(max_length=45)),
                ('conf_value', models.CharField(max_length=100)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('contact_no', models.CharField(max_length=45)),
                ('message', models.TextField()),
                ('note_adm', models.TextField()),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=45)),
                ('percent_off', models.FloatField()),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateTimeField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateTimeField()),
                ('no_of_uses', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='email_template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='payment_gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(max_length=45)),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', models.TextField()),
                ('price', models.FloatField()),
                ('special_price', models.FloatField()),
                ('special_price_from', models.DateField()),
                ('special_price_to', models.DateField()),
                ('status', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('meta_title', models.CharField(max_length=45)),
                ('meta_description', models.TextField()),
                ('meta_keywords', models.TextField()),
                ('status1', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='product_attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modified_by', models.IntegerField()),
                ('modified_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('fb_token', models.CharField(max_length=100)),
                ('twitter_token', models.CharField(max_length=100)),
                ('google_token', models.CharField(max_length=100)),
                ('registration_method', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='user_wish_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
        migrations.CreateModel(
            name='user_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_method', models.IntegerField()),
                ('AWB_No', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('status', models.IntegerField()),
                ('grand_total', models.FloatField()),
                ('shipping_charges', models.FloatField()),
                ('billing_address1', models.CharField(max_length=100)),
                ('billing_address2', models.CharField(max_length=100)),
                ('billing_city', models.CharField(max_length=45)),
                ('billing_state', models.CharField(max_length=45)),
                ('billing_country', models.CharField(max_length=45)),
                ('billing_zipcode', models.CharField(max_length=45)),
                ('shipping_address1', models.CharField(max_length=100)),
                ('shipping_address2', models.CharField(max_length=100)),
                ('shipping_city', models.CharField(max_length=45)),
                ('shipping_state', models.CharField(max_length=45)),
                ('shipping_country', models.CharField(max_length=45)),
                ('shipping_zipcode', models.CharField(max_length=45)),
                ('coupon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.coupon')),
                ('payment_gateway_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.payment_gateway')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
        migrations.CreateModel(
            name='user_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('zipcode', models.CharField(max_length=45)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user')),
            ],
        ),
        migrations.CreateModel(
            name='product_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
                ('product_image', models.ImageField(upload_to='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product')),
            ],
        ),
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.category')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product')),
            ],
        ),
        migrations.CreateModel(
            name='product_attribute_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=45)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modified_by', models.IntegerField()),
                ('modified_date', models.DateField()),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product_attributes')),
            ],
        ),
        migrations.CreateModel(
            name='product_attribute_assoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_attribute_value_id', models.IntegerField()),
                ('product_attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product_attributes')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product')),
            ],
        ),
        migrations.CreateModel(
            name='order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.FloatField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.product')),
            ],
        ),
        migrations.CreateModel(
            name='coupons_used',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('created_date', models.DateField()),
                ('coupon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.coupon')),
            ],
        ),
    ]
