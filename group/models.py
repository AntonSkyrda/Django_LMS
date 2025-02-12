from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=255)
    course_number = models.PositiveIntegerField()
    students = models.ManyToManyField(User, related_name="groups", blank=True)

    def __str__(self):
        return f"{self.name} ({self.course_number})"
