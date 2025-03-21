from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/courses/", include("course.urls")),
    path("api/groups/", include("group.urls")),
    path("api/lessons/", include("lesson.urls")),
    path("api/tasks/", include("task.urls")),
    path("api/users/", include("user.urls")),
]
