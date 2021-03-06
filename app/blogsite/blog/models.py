import random

import string

from time import time

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(string):
    new_slug = slugify(string, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


def gen_random_letters(number):
    r_letters = ''
    for i in range(number):
        r_letters += random.choice(string.printable)
    return r_letters


class Post(models.Model):
    image = models.ImageField(blank=True, upload_to='uploads/')
    title = models.CharField(blank=True, max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True,
                                    related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = gen_random_letters(10)
        if not self.body:
            self.body = gen_random_letters(100)
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

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


class User(models.Model):
    nickname = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def get_absolute_url(self):
        return reverse('user_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('user_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('user_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.nickname)
        super().save(*args, **kwargs)