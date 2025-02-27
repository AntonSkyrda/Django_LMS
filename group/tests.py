from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from group.models import Group
from user.models import User


class GroupAPIViewTest(TestCase):
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

        self.group = Group.objects.create(name="Test Group", year_number=2025)

    def test_group_list_and_create_admin(self):
        self.client.login(username="admin1", password="admin123")

        url = reverse("group:group-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Group")

        data = {
            "name": "New Group",
            "year_number": 2026,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Group")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[1]["name"], "New Group")

    def test_group_create_teacher(self):
        self.client.login(username="teacher1", password="teacher123")

        url = reverse("group:group-list-create")
        data = {
            "name": "New Group",
            "year_number": 2026,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_group_create_student(self):
        self.client.login(username="student1", password="student123")

        url = reverse("group:group-list-create")
        data = {
            "name": "New Group",
            "year_number": 2026,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_group_detail_admin(self):
        self.client.login(username="admin1", password="admin123")

        url = reverse("group:group-detail-update-delete", args=[self.group.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Group")

    def test_group_update_teacher(self):
        self.client.login(username="teacher1", password="teacher123")

        url = reverse("group:group-detail-update-delete", args=[self.group.id])
        data = {"name": "Updated Group Name"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_group_update_student(self):
        self.client.login(username="student1", password="student123")

        url = reverse("group:group-detail-update-delete", args=[self.group.id])
        data = {"name": "Updated Group Name"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_group_delete_admin(self):
        self.client.login(username="admin1", password="admin123")

        url = reverse("group:group-detail-update-delete", args=[self.group.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
