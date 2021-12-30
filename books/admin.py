from django.contrib import admin
from . import models

# Register your models here.

class inlineSubjects(admin.TabularInline):

	model = models.Subject


@admin.register(models.Field)
class fieldAdmin(admin.ModelAdmin):

	""" Field Admin """
	
	inlines = (inlineSubjects,)


class inlineFiles(admin.TabularInline):

	model = models.File


@admin.register(models.Subject)
class subjectAdmin(admin.ModelAdmin):

	""" Subject Admin """
	
	inlines = (inlineFiles,)

@admin.register(models.File)
class fileAdmin(admin.ModelAdmin):
	""" File Admin """

	pass 
