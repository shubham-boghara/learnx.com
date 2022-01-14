from django.core.exceptions import FieldDoesNotExist, ObjectDoesNotExist
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.

def home_view(request):

    fields = models.Field.objects.all()
    field, sem, year = request.GET.get("field",None), request.GET.get("sem",None),request.GET.get("year",None)
    subjects = None

    try:
        get_field = models.Field.objects.get(field_name=field)
        subjects = models.Subject.objects.filter(field=get_field,sem=sem,year=year)
    except ObjectDoesNotExist:
        subjects = None
        
        



    context = {
       "fields":fields,
       "range_sem":range(1,9),
       "range_year":range(1,5),
       "subjects":subjects,
    }
    return render(request,"books/home_view.html",context)


def file_view(request,pk,subject_name):
    get_subject = models.Subject.objects.get(pk=pk,name=subject_name)

    files = get_subject.files.all

    context = {
        "files":files
    } 

    return render(request,"books/files_view.html",context)