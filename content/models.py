from typing import Type
from django.db import models
from django.template.defaultfilters import slugify
from core import models as core_models
from froala_editor.fields import FroalaField


# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80,unique=True)
    slug = models.SlugField(max_length=80,blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CategoryList(AbstractItem):
    """ CategoryList Model """

    class Meta:
        verbose_name_plural = "Categories List"


class SubCategoryList(AbstractItem):
    """ SubCategoryList Model """

    categories_list = models.ManyToManyField("CategoryList", related_name="SubCategoryList", blank=True)

    class Meta:
        verbose_name_plural = "Sub-Categories List"


class Course(core_models.TimeStampedModel):
    """ Course Model """

    title = models.CharField(max_length=251)
    slug = models.SlugField(max_length=251,blank=True)
    description = FroalaField()
    main_photo = models.ImageField(upload_to="courses_main_photo")
    categories = models.ManyToManyField("SubCategoryList", related_name="courses", blank=True)
    host = models.ForeignKey("users.User", related_name="courses", on_delete=models.CASCADE)
    is_showcase = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(core_models.TimeStampedModel):
    """ Review Model"""

    choices = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )

    message = models.CharField(max_length=251)
    course = models.ForeignKey("Course", related_name="reviews", on_delete=models.CASCADE)
    rating = models.CharField(max_length=10, choices=choices)
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)


class Photos(core_models.TimeStampedModel):
    """ Photos Model """

    course = models.ForeignKey("Course", related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="courses_photos")
    alt = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "photos"


class Tag(core_models.TimeStampedModel):
    """ Tag Model """

    name = models.CharField(max_length=20)
    course = models.ForeignKey("Course", related_name="tags", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "tags"
