from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView
from student.api.views import StudentListView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
    path('students/', StudentListView.as_view(), name='student-list'),
]
