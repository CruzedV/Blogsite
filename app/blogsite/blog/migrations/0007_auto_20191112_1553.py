# Generated by Django 2.2.6 on 2019-11-12 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.User')),
                ('first_name', models.CharField(max_length=20)),
            ],
            bases=('blog.user',),
        ),
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
    ]
