from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(string):
    new_slug = slugify(string, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class News(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=30, unique=True)
    text = models.TextField(max_length=400, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, 
                                    related_name='news')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('news_detail_url', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('news_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('news_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
