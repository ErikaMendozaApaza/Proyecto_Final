# Generated by Django 4.2.4 on 2023-09-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_projectcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsection',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servicesection',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]