from rest_framework import generics, permissions
from course.models import Course
from course.serializers import CourseSerializer, CourseDetailSerializer
from user.permissions import IsStudent, IsTeacher, IsAdmin


class CourseListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Course.objects.filter(groups__students=user).distinct()

        if user.role == "teacher":
            return Course.objects.filter(teacher=user)

        return Course.objects.all()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]


class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseDetailSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Course.objects.filter(groups__students=user).distinct()

        if user.role == "teacher":
            return Course.objects.filter(teacher=user)

        return Course.objects.all()

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]
        return [permissions.IsAuthenticated()]
