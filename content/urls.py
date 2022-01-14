from django.urls import path
from .views import CoursesView as course_view
from .views import CoursePageView as course_page_view
from .views import CourseCategoryPageView as course_category_view
from .views import CourseSubCategoryPageView as course_subc_view

app_name = "courses"

urlpatterns = [
    path("", course_view, name="courses_view"),
    path("<int:pk>/<slug:resources_name>/", course_page_view, name="resources"),
    path("categories/<int:pk>/<slug:category_name>", course_category_view, name="category_view"),
    path("categories/<slug:category_name>/<int:pk>/<slug:subcategory_name>", course_subc_view,
         name="subcategory_view"),

]
