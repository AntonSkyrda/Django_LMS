from django.contrib.auth import get_user_model
from django.db import models

from group.models import Group
from course.models import Course

User = get_user_model()


class Lesson(models.Model):
    topic = models.CharField(max_length=255)
    hour_count = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="lessons")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lessons",
        limit_choices_to={"role": "teacher"},
    )

    def __str__(self):
        return f"{self.topic} - {self.group.name} ({self.date})"
