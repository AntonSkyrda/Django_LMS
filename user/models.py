import string
from random import choices

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

    @staticmethod
    def generate_username(first_name, last_name):
        base_username = f"{first_name}_{last_name}".lower()
        username = base_username
        while User.objects.filter(username=username).exists():
            random_suffix = "".join(
                choices(string.ascii_lowercase + string.digits, k=3)
            )
            username = f"{base_username}_{random_suffix}"
        return username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.generate_username(self.first_name, self.last_name)
        super().save(*args, **kwargs)
