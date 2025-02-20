from django.urls import path


from lesson.views import LessonListCreateView, LessonRetrieveUpdateDestroyView

urlpatterns = [
    path("", LessonListCreateView.as_view(), name="lesson-list-create"),
    path(
        "<int:pk>",
        LessonRetrieveUpdateDestroyView.as_view(),
        name="lesson-detail-update-delete",
    ),
]


app_name = "lesson"
