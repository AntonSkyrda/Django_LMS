from django.urls import path


from user.views import (
    TeacherListCreateView,
    TeacherRetrieveUpdateDestroyView,
    StudentListCreateView,
    StudentRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("teachers", TeacherListCreateView.as_view(), name="teachers-list-create"),
    path("students", StudentListCreateView.as_view(), name="students-list-create"),
    path(
        "teachers/<int:pk>",
        TeacherRetrieveUpdateDestroyView.as_view(),
        name="teachers-detail-update-delete",
    ),
    path(
        "students/<int:pk>",
        StudentRetrieveUpdateDestroyView.as_view(),
        name="students-detail-update-delete",
    ),
]


app_name = "user"
