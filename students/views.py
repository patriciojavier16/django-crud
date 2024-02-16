from django.shortcuts import render,redirect
from .models import Students

# Create your views here.
def listStudents(request):
    api_url = 'http://localhost:9090/students'
    response = request.get(api_url)
    if response.status_code == 200:
        students = response.json()
        return render(request, 'listStudent.html',{"students": students})
    else:
        return render(request, 'error.html', {'message': 'Error al obtener datos'})
    

def createStudent(request):
    student = Students(dni=request.POST['dni'],nombre=request.POST['nombre'],apellido=request.POST['apellido'],genero=request.POST['genero'])
    student.save()
    return redirect('/students/')

def deleteStudent(request, student_id):
    student = Students.objects.get(id=student_id)
    student.delete()
    return redirect('/students/')
