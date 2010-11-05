# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Tag(models.Model):
    # Attributs
    designation = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    # Methods
    def __unicode__(self):
        return u'%s' % (self.designation)
    # Meta
    class Meta:
        ordering = ['designation']
        verbose_name, verbose_name_plural = (u'Tag', u'Tags')

class Category(models.Model):
    # Attributes
    designation = models.CharField(u'Désignation', max_length=255)
    parent_category = models.ForeignKey('self', verbose_name='Categorie',
            null=True, blank=True)
    # Methods
    def __unicode__(self):
        return u'%s' % (self.designation)
    # Meta
    class Meta:
        verbose_name, verbose_name_plural = (u'Catégorie', u'Catégories')

class Article(models.Model):
    # Attributes
    title = models.CharField(u'Titre', max_length=255, unique=True)
    author = models.ForeignKey(User, verbose_name=u'Auteur')
    content = models.TextField(u'Contenu')
    category = models.ForeignKey(Category, verbose_name=u'Catégorie')
    tags = generic.GenericRelation(Tag)
    published_state = models.BooleanField(u'Publié', default=0)
    published_date = models.DateTimeField(u'Date de publication', null=True,
            blank=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    # Methods
    def __unicode__(self):
            return u'%s' % (self.title)
    # Meta
    class Meta:
        verbose_name, verbose_name_plural = (u'Article', u'Articles')

class Page(models.Model):
   # Attributes
    title = models.CharField(u'Titre', max_length=255, unique=True)
    author = models.ForeignKey(User, verbose_name=u'Auteur')
    content = models.TextField(u'Contenu')
    published_state = models.BooleanField(u'Publié', default=0)
    published_date = models.DateTimeField(u'Date de publication', null=True,
            blank=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    # Methods
    def __unicode__(self):
            return u'%s' % (self.title)
    # Meta  
    class Meta:
        verbose_name, verbose_name_plural = (u'Page', u'Pages')
