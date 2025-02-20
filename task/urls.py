from django.urls import path


from task.views import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
    SubmissionListCreateView,
    SubmissionRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("", TaskListCreateView.as_view(), name="task-list-create"),
    path("submission", SubmissionListCreateView.as_view(), name="task-list-create"),
    path(
        "<int:pk>",
        TaskRetrieveUpdateDestroyView.as_view(),
        name="task-detail-update-delete",
    ),
    path(
        "submission/<int:pk>",
        SubmissionRetrieveUpdateDestroyView.as_view(),
        name="task-detail-update-delete",
    ),
]


app_name = "task"
