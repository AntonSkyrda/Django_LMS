from django.urls import path


from group.views import GroupListCreateView, GroupRetrieveUpdateDestroyView

urlpatterns = [
    path("groups/", GroupListCreateView.as_view(), name="group-list-create"),
    path(
        "groups/<int:pk>",
        GroupRetrieveUpdateDestroyView.as_view(),
        name="group-detail-update-delete",
    ),
]


app_name = "group"
