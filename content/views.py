from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.paginator import EmptyPage, Paginator
from django.core.exceptions import ObjectDoesNotExist
from . import models



# Create your views here.

def CoursesView(request):
    """ CourseView Definition """

    page_number = request.GET.get("page", 1)
    courses_list = models.Course.objects.all()
    category_list = models.CategoryList.objects.all()
    paginator = Paginator(courses_list, 10, orphans=5)
    num_pages = paginator.num_pages

    try:
        num = num_pages if int(page_number) >= num_pages else page_number
    except ValueError:
        return HttpResponse("Sorry String :(")

    try:
        page = paginator.page(int(num))
    except EmptyPage:
        return HttpResponse("Sorry no more pages")

    context = {
        "page_obj": page,
        "category_obj": category_list
    }
    return render(request, "course/courses_list.html", context)


def CoursePageView(request, resources_name,pk):
    """ CoursePageView Definition """

    try:
        course = models.Course.objects.get(pk=pk)
    except ObjectDoesNotExist:
       return HttpResponse("<h2>Course Doesn't Exist</h2>") 

    
    
    context = {
        "course": course
    }

    return render(request, "course/course_view.html", context)


def CourseCategoryPageView(request, category_name, pk):
    """ CourseCategoryPageView Definition  """

    try:
      category = models.CategoryList.objects.get(pk=pk)
    except ObjectDoesNotExist:
       return HttpResponse("<h2>Category Doesn't Exist</h2>") 

    subcategories = category.SubCategoryList.all


    context = {
        "subcategories_objs": subcategories
    }

    return render(request, "course/category_view.html", context)


def CourseSubCategoryPageView(request,category_name, subcategory_name, pk):
    """ CourseSubCategoryPageView definition """

    try:
        subcategory = models.SubCategoryList.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse("<h2>Category Doesn't Exist</h2>")

    courses = subcategory.courses.all
   

    context = {
        "courses": courses
    }

    return render(request, "course/subcategory_view.html", context)
