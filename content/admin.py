from django.contrib import admin
from . import models 

# Register your models here.

@admin.register(models.CategoryList)
class modelAdmin(admin.ModelAdmin):
	""" Category Admin """
	pass


@admin.register(models.SubCategoryList)
class subCategoryAdmin(admin.ModelAdmin):
   """ Subject Admin """

   filter_horizontal = ("categories_list",)



class PhotoInline(admin.TabularInline):

    model = models.Photos

class TagInline(admin.TabularInline):

    model = models.Tag    

@admin.register(models.Course)
class courseAdmin(admin.ModelAdmin):
    """ Course Admin """

    inlines = (PhotoInline,TagInline)
    filter_horizontal = ("categories",)


@admin.register(models.Review)
class reviewAdmin(admin.ModelAdmin):
	""" Review Admin """
	pass


@admin.register(models.Photos)
class photoAdmin(admin.ModelAdmin):
	""" Photo Admin """
	pass


@admin.register(models.Tag)
class tagAdmin(admin.ModelAdmin):
	""" Tag Admin """
	pass


