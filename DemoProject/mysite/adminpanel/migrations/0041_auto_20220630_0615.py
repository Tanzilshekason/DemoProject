# Generated by Django 3.2.12 on 2022-06-30 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0040_contactus_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='contact_no',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='modify_by',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='modify_date',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='note_adm',
        ),
    ]
