# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Document, School
# Register your models here.
@admin.register(Document)
class AdminDocuments(admin.ModelAdmin):
	list_display = ('id',)

@admin.register(School)
class AdminSchools(admin.ModelAdmin):
	list_display = ('name',)