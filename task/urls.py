from django.urls import path


from task.views import (
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
    SubmissionListCreateView,
    SubmissionRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("task/", TaskListCreateView.as_view(), name="task-list-create"),
    path(
        "task/submission", SubmissionListCreateView.as_view(), name="task-list-create"
    ),
    path(
        "task/<int:pk>",
        TaskRetrieveUpdateDestroyView.as_view(),
        name="task-detail-update-delete",
    ),
    path(
        "task/submission/<int:pk>",
        SubmissionRetrieveUpdateDestroyView.as_view(),
        name="task-detail-update-delete",
    ),
]


app_name = "task"
