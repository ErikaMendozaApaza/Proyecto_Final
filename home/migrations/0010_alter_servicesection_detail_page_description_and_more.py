# Generated by Django 4.2.4 on 2023-09-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_aboutsection_image_aboutsection_video_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesection',
            name='detail_page_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicesection',
            name='detail_page_image',
            field=models.ImageField(blank=True, null=True, upload_to='Services/'),
        ),
    ]
