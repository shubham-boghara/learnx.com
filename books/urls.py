from django.urls.conf import path
from .views import home_view,file_view

app_name = "books"

urlpatterns = [
    path("",home_view,name="home_view"),
    path("files/<int:pk>/<str:subject_name>/",file_view,name="files_view")

]
