# Generated by Django 3.2.12 on 2022-06-09 06:09

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_path', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('images', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'banners',
                'verbose_name_plural': 'banners',
            },
        ),
        migrations.CreateModel(
            name='Category',
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
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'category',
            },
        ),
        migrations.CreateModel(
            name='Cms',
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
            options={
                'verbose_name': 'cms',
                'verbose_name_plural': 'cms',
            },
        ),
        migrations.CreateModel(
            name='Configuration',
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
            options={
                'verbose_name': 'configuration',
                'verbose_name_plural': 'configuration',
            },
        ),
        migrations.CreateModel(
            name='Contact_us',
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
            options={
                'verbose_name': 'contact_us',
                'verbose_name_plural': 'contact_us',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
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
            options={
                'verbose_name': 'coupon',
                'verbose_name_plural': 'coupon',
            },
        ),
        migrations.CreateModel(
            name='Email_template',
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
            options={
                'verbose_name': 'email_template',
                'verbose_name_plural': 'email_template',
            },
        ),
        migrations.CreateModel(
            name='Manage_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment_gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
            ],
            options={
                'verbose_name': 'payment_gateway',
                'verbose_name_plural': 'payment_gateway',
            },
        ),
        migrations.CreateModel(
            name='Product',
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
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'product',
            },
        ),
        migrations.CreateModel(
            name='Product_attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modified_by', models.IntegerField()),
                ('modified_date', models.DateField()),
            ],
            options={
                'verbose_name': 'product_attributes',
                'verbose_name_plural': 'product_attributes',
            },
        ),
        migrations.CreateModel(
            name='User_info',
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
            options={
                'verbose_name': 'user_info',
                'verbose_name_plural': 'user_info',
            },
        ),
        migrations.CreateModel(
            name='User_wish_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.user_info')),
            ],
            options={
                'verbose_name': 'user_wish_list',
                'verbose_name_plural': 'user_wish_list',
            },
        ),
        migrations.CreateModel(
            name='User_order',
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
                ('coupon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.coupon')),
                ('payment_gateway_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.payment_gateway')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.user_info')),
            ],
            options={
                'verbose_name': 'user_order',
                'verbose_name_plural': 'user_order',
            },
        ),
        migrations.CreateModel(
            name='User_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('zipcode', models.CharField(max_length=45)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.user_info')),
            ],
            options={
                'verbose_name': 'user_address',
                'verbose_name_plural': 'user_address',
            },
        ),
        migrations.CreateModel(
            name='Product_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modify_by', models.IntegerField()),
                ('modify_date', models.DateField()),
                ('product_image', models.ImageField(upload_to='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product')),
            ],
            options={
                'verbose_name': 'product_images',
                'verbose_name_plural': 'product_images',
            },
        ),
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.category')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product')),
            ],
            options={
                'verbose_name': 'product_category',
                'verbose_name_plural': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='Product_attribute_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=45)),
                ('created_by', models.IntegerField()),
                ('created_date', models.DateField()),
                ('modified_by', models.IntegerField()),
                ('modified_date', models.DateField()),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product_attributes')),
            ],
            options={
                'verbose_name': 'product_attribute_value',
                'verbose_name_plural': 'product_attribute_value',
            },
        ),
        migrations.CreateModel(
            name='Product_attribute_assoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_attribute_value_id', models.IntegerField()),
                ('product_attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product_attributes')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product')),
            ],
            options={
                'verbose_name': 'product_attribute_assoc',
                'verbose_name_plural': 'product_attribute_assoc',
            },
        ),
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.FloatField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.product')),
            ],
            options={
                'verbose_name': 'order_details',
                'verbose_name_plural': 'order_details',
            },
        ),
        migrations.CreateModel(
            name='Coupons_used',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('created_date', models.DateField()),
                ('coupon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.coupon')),
            ],
            options={
                'verbose_name': 'coupons_used',
                'verbose_name_plural': 'coupons_used',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_customer', models.BooleanField(default=False, verbose_name='Is customer')),
                ('is_order', models.BooleanField(default=False, verbose_name='Is order')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
