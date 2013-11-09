#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from django.contrib import admin
from library.models import *


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email']
    list_display_links = ['last_name', 'first_name']
    ordering = ['last_name', 'first_name']


class ImageInline(generic.GenericTabularInline):
    model = BookImage
    extra = 0


class BooksAdmin(admin.ModelAdmin):
    def covers_count(self, obj):
        i = 0
        for c in BookImage.objects.filter(id=obj.id):
            if c.small_image:
                i+= 1
            if c.large_image:
                i+= 1
        return i
    covers_count.allow_tags = True

    def get_img_cover(self, obj):
        link = ""
        for c in BookImage.objects.filter(id=obj.id):
            link = c.img_tag()
        return link
    get_img_cover.allow_tags = True

    def get_large_img_cover(self, obj):
        link = ""
        for c in BookImage.objects.filter(id=obj.id):
            link = c.img_tag()
        return link
    get_large_img_cover.allow_tags = True

    list_display = ['title', 'publisher', 'publication_date',
                    'covers_count', 'get_img_cover', 'get_large_img_cover', ]
    list_display_links = ['title']
    search_fields = ['title']
    date_hierarchy = 'publication_date'
    fieldsets = (
        (None, {'fields': ('title', 'authors', 'publication_date',)}),
        ('Output data', {
            'classes': ('wide',),
            'description': 'Information about publisher',
            'fields': ('publisher',),
        }),
    )
    filter_horizontal = ('authors',)
    inlines = [ImageInline, ]


class PublishersAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city']
    list_display_links = ['title']
    ordering = ['title']
    list_filter = ['country', 'city']
    fieldsets = (
        (None, {'fields': ('title',)}),
        ('Contact infromation', {
            'classes': ('wide',),
            'description': 'Contact information',
            'fields': ('country', 'city', 'address'),
        }),
    )


class BookImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_cover', 'img_tag', 'large_img_tag']


admin.site.register(Book, BooksAdmin)
admin.site.register(BookImage, BookImageAdmin)
admin.site.register(Author, AuthorsAdmin)
admin.site.register(Publisher, PublishersAdmin)
