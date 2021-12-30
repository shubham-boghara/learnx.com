from django.contrib import admin
from . import models
from content.models import Course
# Register your models here.

class contentInline(admin.TabularInline):

	model = Course

@admin.register(models.User)
class userAdmin(admin.ModelAdmin):
	
	inlines = (contentInline,)