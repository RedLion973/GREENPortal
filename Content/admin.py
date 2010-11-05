from django.contrib import admin
from django.contrib.contenttypes import generic
from GREENPortal.Content.models import *

class TagInline(generic.GenericStackedInline):
    model = Tag
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
            TagInline,
            ]

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Page)
