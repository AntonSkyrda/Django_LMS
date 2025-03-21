from rest_framework import generics, permissions
from lesson.models import Lesson
from lesson.serializers import LessonSerializer, LessonDetailSerializer
from user.permissions import IsStudent, IsTeacher, IsAdmin


class LessonListCreateView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Lesson.objects.filter(group__students=user).distinct()

        if user.role == "teacher":
            return Lesson.objects.filter(course__teacher=user)

        return Lesson.objects.all()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsTeacher()]
        return [permissions.IsAuthenticated()]


class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = LessonDetailSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Lesson.objects.filter(group__students=user).distinct()

        if user.role == "teacher":
            return Lesson.objects.filter(course__teacher=user)

        return Lesson.objects.all()

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsTeacher()]
        return [permissions.IsAuthenticated()]
