# Generated by Django 2.2.6 on 2020-02-07 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
    ]
