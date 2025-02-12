from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("teacher", "Teacher"),
        ("student", "Student"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def is_teacher(self):
        return self.role == "teacher"

    def is_student(self):
        return self.role == "student"

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
