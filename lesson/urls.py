from django.urls import path


from lesson.views import LessonListCreateView, LessonRetrieveUpdateDestroyView

urlpatterns = [
    path("lessons/", LessonListCreateView.as_view(), name="lesson-list-create"),
    path(
        "lessons/<int:pk>",
        LessonRetrieveUpdateDestroyView.as_view(),
        name="lesson-detail-update-delete",
    ),
]


app_name = "lesson"
