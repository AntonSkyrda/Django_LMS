from django.contrib.auth import get_user_model
from django.db import models

from group.models import Group


User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    teacher = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="courses"
    )
    groups = models.ManyToManyField(Group, related_name="courses", blank=True)

    def __str__(self):
        return self.name
