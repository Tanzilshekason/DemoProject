# Generated by Django 3.2.12 on 2022-06-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0005_auto_20220616_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'User_login',
                'verbose_name_plural': 'User_login',
            },
        ),
    ]
