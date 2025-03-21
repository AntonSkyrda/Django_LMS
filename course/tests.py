from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from course.models import Course
from user.models import User


class CourseAPIViewTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin1", password="admin123", is_superuser=True
        )

        self.teacher = User.objects.create_user(
            username="teacher1", password="teacher123", role="teacher"
        )

        self.student = User.objects.create_user(
            username="student1", password="student123", role="student"
        )

        self.course = Course.objects.create(
            name="Test Course", description="Test Description", teacher=self.teacher
        )

    def test_course_list_and_create_admin(self):
        self.client.login(username="admin1", password="admin123")

        url = reverse("courses:course-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Course")

        data = {
            "name": "New Course",
            "description": "New Course Description",
            "teacher": self.teacher.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Course")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[1]["name"], "New Course")

    def test_course_create_teacher(self):
        self.client.login(username="teacher1", password="teacher123")

        url = reverse("courses:course-list-create")
        data = {
            "name": "New Course",
            "description": "New Course Description",
            "teacher": self.teacher.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_course_create_student(self):
        self.client.login(username="student1", password="student123")

        url = reverse("courses:course-list-create")
        data = {
            "name": "New Course",
            "description": "New Course Description",
            "teacher": self.teacher.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_course_detail_admin(self):
        self.client.login(username="admin1", password="admin123")

        url = reverse("courses:course-detail-update-delete", args=[self.course.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Course")

    def test_course_detail_teacher(self):
        self.client.login(username="teacher1", password="teacher123")

        url = reverse("courses:course-detail-update-delete", args=[self.course.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Course")

    def test_course_update_teacher(self):
        self.client.login(username="teacher1", password="teacher123")

        url = reverse("courses:course-detail-update-delete", args=[self.course.id])
        data = {"name": "Updated Course Name"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_course_update_student(self):
        self.client.login(username="student1", password="student123")

        url = reverse("courses:course-detail-update-delete", args=[self.course.id])
        data = {"name": "Updated Course Name"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_course_delete_admin(self):
        self.client.login(username="admin1", password="admin123")

        url = reverse("courses:course-detail-update-delete", args=[self.course.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
