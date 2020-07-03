from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("kanban/", include("kanban.urls")),
    path("kanban/", include("django.contrib.auth.urls")),
]
