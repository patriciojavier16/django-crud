from django.shortcuts import render,redirect
from .models import Students

# Create your views here.
def listStudents(request):
    students = Students.objects.all()
    return render(request, 'listStudent.html',{"students": students})

def createStudent(request):
    student = Students(dni=request.POST['dni'],nombre=request.POST['nombre'],apellido=request.POST['apellido'])
    student.save()
    return redirect('/students/')

def deleteStudent(request, student_id):
    student = Students.objects.get(id=student_id)
    student.delete()
    return redirect('/students/')
