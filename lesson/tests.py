from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from lesson.models import Lesson
from user.models import User
from group.models import Group
from course.models import Course


class LessonAPITestCase(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(
            username="teacher", password="password", role="teacher"
        )
        self.student = User.objects.create_user(
            username="student", password="password", role="student"
        )

        self.group = Group.objects.create(name="Test Group", year_number=2025)

        self.course = Course.objects.create(name="Test Course", teacher=self.teacher)

        self.group.students.add(self.student)

        self.lesson = Lesson.objects.create(
            topic="Test Lesson",
            hour_count=2,
            date="2025-03-01",
            time="10:00:00",
            group=self.group,
            course=self.course,
            teacher=self.teacher,
        )

    def test_get_lessons_as_student(self):
        self.client.login(username="student", password="password")

        url = reverse("lesson:lesson-list-create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["topic"], "Test Lesson")

    def test_get_lessons_as_teacher(self):
        self.client.login(username="teacher", password="password")

        url = reverse("lesson:lesson-list-create")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["topic"], "Test Lesson")

    def test_create_lesson_as_teacher(self):
        self.client.login(username="teacher", password="password")

        data = {
            "topic": "New Test Lesson",
            "hour_count": 3,
            "date": "2025-03-02",
            "time": "11:00:00",
            "group": self.group.id,
            "course": self.course.id,
            "teacher": self.teacher.id,
        }

        url = reverse("lesson:lesson-list-create")
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["topic"], "New Test Lesson")

    def test_delete_lesson_as_teacher(self):
        self.client.login(username="teacher", password="password")

        url = reverse("lesson:lesson-detail-update-delete", args=[self.lesson.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

    def test_access_lessons_as_non_teacher(self):
        self.client.login(username="student", password="password")

        url = reverse("lesson:lesson-list-create")
        data = {
            "topic": "Unauthorized Lesson",
            "hour_count": 2,
            "date": "2025-03-02",
            "time": "10:00:00",
            "group": self.group.id,
            "course": self.course.id,
            "teacher": self.teacher.id,
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
