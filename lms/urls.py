from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("course.urls")),
    path("api/", include("group.urls")),
    path("api/", include("lesson.urls")),
    path("api/", include("task.urls")),
    path("api/users/", include("user.urls")),
]
