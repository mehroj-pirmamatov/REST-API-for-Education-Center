from django.urls import path
from .views import (
    CourseListCreateView, CourseDetailView,
    TeacherListCreateView, TeacherDetailView
)

urlpatterns = [
    path('', CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
]