from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from courses.models import Course, Teacher, Group
from students.models import Student

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()
        data = {
            "students_count": Student.objects.count(),
            "teachers_count": Teacher.objects.count(),
            "courses_count": Course.objects.count(),
            "groups_count": Group.objects.count(),
            "active_groups_count": Group.objects.filter(start_date__lte=today, end_date__gte=today).count(),
        }
        return Response(data)
