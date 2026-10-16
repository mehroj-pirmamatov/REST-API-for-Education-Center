from django.urls import path
from .views import (
    StudentListCreateView, StudentDetailView,
    EnrollmentListCreateView, EnrollmentDetailView,
    PaymentListCreateView, PaymentDetailView,
    AttendanceListCreateView, AttendanceDetailView
)

urlpatterns = [
    path('', StudentListCreateView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-detail'),
    
    path('payments/', PaymentListCreateView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    
    path('attendances/', AttendanceListCreateView.as_view(), name='attendance-list'),
    path('attendances/<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
]