from rest_framework import generics

from user.models import User
from user.serializers import UserSerializer


class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().filter(role="teacher")
    serializer_class = UserSerializer


class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().filter(role="teacher")
    serializer_class = UserSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().filter(role="student")
    serializer_class = UserSerializer


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().filter(role="student")
    serializer_class = UserSerializer
