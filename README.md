# Blogsite
First Django Project

Documentation

The site include the following packages:
Django==2.2.6
Pillow==7.0.0
psycopg2==2.8.3
pytz==2019.3
sqlparse==0.3.0

Relationships are distributed the next way:

Blogsite distributes a utils for two apps:

blog, containing posts, tags and other stuff such as html, models, forms for them

blog_homepage, containing registration, login, logout logic and news.

Each app contain views, html, models for self needs
