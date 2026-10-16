from rest_framework import serializers
from .models import Course, Teacher, Group

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    course_name = serializers.ReadOnlyField(source='course.name')
    teacher_name = serializers.ReadOnlyField(source='teacher.full_name')

    class Meta:
        model = Group
        fields = '__all__'