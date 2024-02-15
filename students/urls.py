from django.urls import path
from .views import listStudents, createStudent, deleteStudent

urlpatterns = [
    path('', listStudents),
    path('newStudent/', createStudent, name='createStudent'),
    path('deleteStudent/<int:student_id>/', deleteStudent, name='deleteStudent')
]
