from django.contrib.auth import get_user_model
from django.db import models
from course.models import Course
from group.models import Group


User = get_user_model()


class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignments"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="assignments"
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="assignments"
    )

    class Meta:
        unique_together = ("teacher", "course", "group")

    def __str__(self):
        return (
            f"{self.teacher.get_full_name()} - {self.course.name} ({self.group.name})"
        )
