# Generated by Django 2.2.6 on 2019-12-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191112_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=400)),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='news', to='blog.Tag')),
            ],
        ),
        migrations.DeleteModel(
            name='BlogUser',
        ),
    ]