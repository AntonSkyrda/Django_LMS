from django.contrib.auth import get_user_model
from django.db import models

from lesson.models import Lesson


User = get_user_model()


class Task(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (lesson: {self.lesson.topic})"


class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions",
    )
    text_answer = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.PositiveIntegerField(blank=True, null=True)
    graded = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"{self.student.first_name} {self.student.last_name}"
            f" - {self.task.title} ({'Graded' if self.graded else 'Not graded'})"
        )
