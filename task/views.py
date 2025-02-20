from rest_framework import generics, permissions

from task.models import Task, Submission
from task.serializers import (
    TaskSerializer,
    SubmissionSerializer,
    SubmissionDetailSerializer,
)
from user.permissions import IsStudent, IsTeacher, IsAdmin


class TaskListCreateView(generics.ListCreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = [IsTeacher | IsAdmin]

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Task.objects.filter(lesson__group__students=user)

        return Task.objects.filter(lesson__course__teacher=user)

    def perform_create(self, serializer):
        serializer.save()


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsTeacher | IsAdmin]

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Task.objects.filter(lesson__group__students=user)

        return Task.objects.filter(lesson__course__teacher=user)


class SubmissionListCreateView(generics.ListCreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated, IsStudent | IsTeacher | IsAdmin]

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Submission.objects.filter(student=user)

        return Submission.objects.filter(task__lesson__course__teacher=user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class SubmissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = SubmissionDetailSerializer
    permission_classes = [IsStudent | IsTeacher | IsAdmin]

    def get_queryset(self):
        user = self.request.user

        if user.role == "student":
            return Submission.objects.filter(student=user)

        return Submission.objects.filter(task__lesson__course__teacher=user)
