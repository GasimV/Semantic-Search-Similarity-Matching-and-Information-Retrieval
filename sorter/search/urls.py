from django.contrib import admin
from django.urls import path
from .views import Doccument_sorted, search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Doccument_sorted.as_view(), name="index"),
    path("search/", search_view, name="search"),
]