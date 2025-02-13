from rest_framework import serializers


from task.models import Task, Submission
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "lesson", "title", "description", "due_date", "created_at"]


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ("task", "student", "text_answer", "submitted_at", "grade", "graded")


class SubmissionDetailSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)
    student = UserSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = ("task", "student", "text_answer", "submitted_at", "grade", "graded")
