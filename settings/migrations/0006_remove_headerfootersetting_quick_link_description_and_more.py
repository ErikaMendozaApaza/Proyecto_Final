# Generated by Django 4.2.4 on 2023-09-04 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_rename_logo_websitesetting_logo_dark_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerfootersetting',
            name='quick_link_description',
        ),
        migrations.RemoveField(
            model_name='headerfootersetting',
            name='quick_link_title',
        ),
    ]
