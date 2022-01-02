from django.db import models
from core import models as core_models
from froala_editor.fields import FroalaField

# Create your models here.

class Field(core_models.TimeStampedModel):

	""" Field Model """

	field_name = models.CharField(max_length = 50)




class Subject(core_models.TimeStampedModel):

     """ Subject Model """

     field = models.ForeignKey("Field",on_delete = models.CASCADE)
     
     sem_choices = (
          ("1","1"),
          ("2","2"),
          ("3","3"),
          ("4","4"),
          ("5","5"),
          ("6","6"),
          ("7","7"),
          ("8","8"),
     	)

     sem = models.CharField(max_length = 10,choices = sem_choices)

     year_choices = (
          ("1","1"),
          ("2","2"),
          ("3","3"),
          ("4","4"),
     	)

     year = models.CharField(max_length = 10,choices = year_choices)

     name = models.CharField(max_length = 100)


class File(core_models.TimeStampedModel):
 
      """ File  Model """ 

      title = models.CharField(max_length = 251)
      description  = FroalaField()
      subject = models.ForeignKey("Subject", on_delete = models.CASCADE)
      file = models.FileField(upload_to = "books_files",null = True, blank = True)
      is_public = models.BooleanField(default = False)


