from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static





urlpatterns = [
    path("", include("core.urls", namespace = "home")),
    path("resources/", include("content.urls", namespace = "courses")),
    path("books/", include("books.urls", namespace="books")),
    path('admin/', admin.site.urls),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)