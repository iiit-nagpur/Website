# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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

class Adjunctfac(models.Model):
	name=models.CharField(max_length=40)
	post=models.TextField()
	about_fac=models.TextField()
	email=models.EmailField(max_length=40)
	phone=models.CharField(max_length=15)

class Staff(models.Model):
	name=models.CharField(max_length=40)
	post=models.TextField()
	about_fac=models.TextField()
	email=models.EmailField(max_length=40)
	phone=models.CharField(max_length=15)

class Faq(models.Model):
	question = models.TextField()
	answer = models.TextField()

class Student(models.Model):
	name=models.CharField(max_length=40)
	branch=models.CharField(max_length=40)
	program=models.CharField(max_length=40)
	rollno=models.CharField(max_length=10)
	status=models.BooleanField(help_text = "Check if passed out")

class alumni(models.Model):
	name=models.CharField(max_length=40)
	branch=models.CharField(max_length=40)
	about=models.TextField()
	email=models.EmailField(max_length=40)

class departments(models.Model):
	dep_name=models.CharField(max_length=50)
	prof_name=models.CharField(max_length=50)
	prof_image=models.ImageField(upload_to='static/images/')
	prof_degree=models.CharField(max_length=50)
	prof_interest=models.CharField(max_length=50)

class programmes(models.Model):
	program_name=models.CharField(max_length=50)
	about_program=models.TextField()

class convocation(models.Model):
	year=models.IntegerField()
	about=models.TextField()
