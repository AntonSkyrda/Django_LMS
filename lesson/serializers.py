from rest_framework import serializers

from course.serializers import CourseDetailSerializer
from lesson.models import Lesson
from group.serializers import GroupDetailSerializer
from user.serializers import UserSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "topic",
            "hour_count",
            "date",
            "time",
            "group",
            "course",
            "teacher",
        ]


class LessonDetailSerializer(serializers.ModelSerializer):

    group = GroupDetailSerializer()
    course = CourseDetailSerializer()
    teacher = UserSerializer()

    class Meta:
        model = Lesson
        fields = [
            "id",
            "topic",
            "hour_count",
            "date",
            "time",
            "group",
            "course",
            "teacher",
        ]
