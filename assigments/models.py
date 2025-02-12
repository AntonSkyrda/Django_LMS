from django.db import models
from user.models import User
from course.models import Course
from group.models import Group


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
