# Generated by Django 4.0.4 on 2022-05-12 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_rename_img_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]