# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class About(models.Model):
	head = models.CharField(max_length=100)
	content = models.TextField()

class Faculty(models.Model):
	name=models.CharField(max_length=40)
	post=models.TextField()
	about_fac=models.TextField()
	email=models.EmailField(max_length=40)
	phone=models.TextField()
