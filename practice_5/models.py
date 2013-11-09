# Create your models here.
import os
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db import connection
import datetime
from control_panel.settings import PROJECT_ROOT, MEDIA_ROOT, MEDIA_URL


class Author(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):

    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())

    def get_absolute_url(self):
        curson = connection.cursor()
        curson.execute("SELECT id FROM library_book WHERE title = %s", [self.title])
        return "/library/books/%s/" % curson.fetchall()[0]

    def __unicode__(self):
        return self.title

# Create your models here.
import os
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db import connection
import datetime
from control_panel.settings import PROJECT_ROOT, MEDIA_ROOT, MEDIA_URL


class Author(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):

    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())

    def get_absolute_url(self):
        curson = connection.cursor()
        curson.execute("SELECT id FROM library_book WHERE title = %s", [self.title])
        return "/library/books/%s/" % curson.fetchall()[0]

    def __unicode__(self):
        return self.title


class Publisher(models.Model):

    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField(max_length=32)

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.title, self.city, self.country)


class BookImage(models.Model):

    small_image = models.ImageField(upload_to=MEDIA_ROOT)
    large_image = models.ImageField(
        blank=True, null=True, upload_to=MEDIA_ROOT)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    book_cover = models.ForeignKey('Book')

    def __unicode__(self):
        return "%s" % self.id

    def image_count(self):
        i = 0
        if self.small_image:
            i+=1
        elif self.large_image:
            i+=1
        return "%s" % i

    def img_tag(self):
        return '<img src="%s%s"/>' % (MEDIA_URL, os.path.basename(self.small_image.name))
    img_tag.allow_tags = True

    def large_img_tag(self):
        return '<img src="%s%s"/>' % (MEDIA_URL, os.path.basename(self.large_image.name))
    large_img_tag.allow_tags = True


class Publisher(models.Model):

    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField(max_length=32)

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.title, self.city, self.country)


class BookImage(models.Model):

    small_image = models.ImageField(upload_to=MEDIA_ROOT)
    large_image = models.ImageField(
        blank=True, null=True, upload_to=MEDIA_ROOT)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    book_cover = models.ForeignKey('Book')

    def __unicode__(self):
        return "%s" % self.id

    def image_count(self):
        i = 0
        if self.small_image:
            i+=1
        elif self.large_image:
            i+=1
        return "%s" % i

    def img_tag(self):
        return '<img src="%s%s"/>' % (MEDIA_URL, os.path.basename(self.small_image.name))
    img_tag.allow_tags = True

    def large_img_tag(self):
        return '<img src="%s%s"/>' % (MEDIA_URL, os.path.basename(self.large_image.name))
    large_img_tag.allow_tags = True