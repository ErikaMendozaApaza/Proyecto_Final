# Generated by Django 4.2.4 on 2023-09-20 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
