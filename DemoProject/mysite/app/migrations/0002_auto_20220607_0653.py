# Generated by Django 3.2.12 on 2022-06-07 06:53

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
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
        migrations.AlterModelOptions(
            name='banners',
            options={'verbose_name': 'banners', 'verbose_name_plural': 'banners'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'category'},
        ),
        migrations.AlterModelOptions(
            name='cms',
            options={'verbose_name': 'cms', 'verbose_name_plural': 'cms'},
        ),
        migrations.AlterModelOptions(
            name='configuration',
            options={'verbose_name': 'configuration', 'verbose_name_plural': 'configuration'},
        ),
        migrations.AlterModelOptions(
            name='contact_us',
            options={'verbose_name': 'contact_us', 'verbose_name_plural': 'contact_us'},
        ),
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'coupon', 'verbose_name_plural': 'coupon'},
        ),
        migrations.AlterModelOptions(
            name='coupons_used',
            options={'verbose_name': 'coupons_used', 'verbose_name_plural': 'coupons_used'},
        ),
        migrations.AlterModelOptions(
            name='email_template',
            options={'verbose_name': 'email_template', 'verbose_name_plural': 'email_template'},
        ),
        migrations.AlterModelOptions(
            name='order_details',
            options={'verbose_name': 'order_details', 'verbose_name_plural': 'order_details'},
        ),
        migrations.AlterModelOptions(
            name='payment_gateway',
            options={'verbose_name': 'payment_gateway', 'verbose_name_plural': 'payment_gateway'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'product'},
        ),
        migrations.AlterModelOptions(
            name='product_attribute_assoc',
            options={'verbose_name': 'product_attribute_assoc', 'verbose_name_plural': 'product_attribute_assoc'},
        ),
        migrations.AlterModelOptions(
            name='product_attribute_value',
            options={'verbose_name': 'product_attribute_value', 'verbose_name_plural': 'product_attribute_value'},
        ),
        migrations.AlterModelOptions(
            name='product_attributes',
            options={'verbose_name': 'product_attributes', 'verbose_name_plural': 'product_attributes'},
        ),
        migrations.AlterModelOptions(
            name='product_category',
            options={'verbose_name': 'product_category', 'verbose_name_plural': 'product_category'},
        ),
        migrations.AlterModelOptions(
            name='product_images',
            options={'verbose_name': 'product_images', 'verbose_name_plural': 'product_images'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='user_address',
            options={'verbose_name': 'user_address', 'verbose_name_plural': 'user_address'},
        ),
        migrations.AlterModelOptions(
            name='user_order',
            options={'verbose_name': 'user_order', 'verbose_name_plural': 'user_order'},
        ),
        migrations.AlterModelOptions(
            name='user_wish_list',
            options={'verbose_name': 'user_wish_list', 'verbose_name_plural': 'user_wish_list'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fb_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='google_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='registration_method',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='twitter_token',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Is admin'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name='Is customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Is employee'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user_info'),
        ),
        migrations.AlterField(
            model_name='user_order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user_info'),
        ),
        migrations.AlterField(
            model_name='user_wish_list',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user_info'),
        ),
    ]
