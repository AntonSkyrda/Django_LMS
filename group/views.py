from rest_framework import generics, permissions
from group.models import Group
from group.serializers import GroupSerializer, GroupDetailSerializer
from user.permissions import IsAdmin


class GroupListCreateView(generics.ListCreateAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Group.objects.filter(students=user)

        if user.role == "teacher":
            return Group.objects.filter(courses__teacher=user)

        return Group.objects.all()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]


class GroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupDetailSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Group.objects.filter(students=user)

        if user.role == "teacher":
            return Group.objects.filter(courses__teacher=user)

        return Group.objects.all()

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]
