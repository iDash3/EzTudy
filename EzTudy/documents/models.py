# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Document(models.Model):
	school = models.ForeignKey(School, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=10)
	file = models.FileField()

	def __str__(self):
		return self.name