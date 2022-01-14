from django.urls import path
from .views import home as home_view

app_name = "core"

urlpatterns = [path("", home_view ,name="core")]