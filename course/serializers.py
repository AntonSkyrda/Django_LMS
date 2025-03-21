from rest_framework import serializers

from course.models import Course
from group.serializers import GroupDetailSerializer, GroupSerializer
from user.serializers import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "teacher",
            "groups",
        ]


class CourseDetailSerializer(serializers.ModelSerializer):

    groups = GroupDetailSerializer(many=True)
    teacher = UserSerializer()

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "description",
            "teacher",
            "groups",
        ]
