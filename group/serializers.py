from rest_framework import serializers

from group.models import Group
from user.serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name", "year_number", "students")


class GroupDetailSerializer(serializers.ModelSerializer):
    students = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = ("id", "name", "year_number", "students")
