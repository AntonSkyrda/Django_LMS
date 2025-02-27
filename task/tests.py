from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from task.models import Task, Submission
from lesson.models import Lesson
from group.models import Group
from course.models import Course
from user.models import User
from django.utils import timezone


class TaskAPITestCase(APITestCase):

    def setUp(self):
        # Створення користувачів
        self.teacher = User.objects.create_user(
            username="teacher", password="password", role="teacher"
        )
        self.student = User.objects.create_user(
            username="student", password="password", role="student"
        )

        # Створення курсу
        self.course = Course.objects.create(name="Test Course", teacher=self.teacher)

        # Створення групи
        self.group = Group.objects.create(name="Test Group", year_number=2025)

        # Створення уроку
        self.lesson = Lesson.objects.create(
            topic="Test Lesson",
            hour_count=2,
            date=timezone.now().date(),
            time=timezone.now().time(),
            course=self.course,  # вказуємо курс
            group=self.group,  # вказуємо групу
            teacher=self.teacher,
        )

        # Створення завдання для уроку
        self.task = Task.objects.create(
            lesson=self.lesson,
            title="Test Task",
            description="This is a test task",
            due_date=timezone.now() + timezone.timedelta(days=1),
        )

    def test_create_task_as_teacher(self):
        self.client.login(username="teacher", password="password")
        url = reverse("task:task-list-create")  # Використовуємо правильний шлях
        data = {
            "lesson": self.lesson.id,
            "title": "New Task",
            "description": "New task description",
            "due_date": timezone.now() + timezone.timedelta(days=2),
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_create_task_as_student(self):
        self.client.login(username="student", password="password")
        url = reverse("task:task-list-create")  # Використовуємо правильний шлях
        data = {
            "lesson": self.lesson.id,
            "title": "New Task",
            "description": "New task description",
            "due_date": timezone.now() + timezone.timedelta(days=2),
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_task_as_teacher(self):
        self.client.login(username="teacher", password="password")
        url = reverse(
            "task:task-detail-update-delete", kwargs={"pk": self.task.id}
        )  # Правильний шлях для оновлення
        data = {"title": "Updated Task", "description": "Updated task description"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Task")

    def test_delete_task_as_teacher(self):
        self.client.login(username="teacher", password="password")
        url = reverse(
            "task:task-detail-update-delete", kwargs={"pk": self.task.id}
        )  # Правильний шлях для видалення
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_submission_creation(self):
        # Створення submission для студента
        self.client.login(username="student", password="password")
        url = reverse(
            "task:submission-list-create"
        )  # Правильний шлях для створення submission
        data = {
            "task": self.task.id,
            "text_answer": "This is my submission",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Submission.objects.count(), 1)
        submission = Submission.objects.first()
        self.assertEqual(submission.student, self.student)
        self.assertEqual(submission.task, self.task)
