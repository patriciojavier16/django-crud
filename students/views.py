from django.shortcuts import render,redirect
from .models import Students
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def listStudents(request):
#     students = Students.objects.all()
#     return render(request, 'listStudent.html',{"students": students})
def listStudents(request):
    api_url = 'http://localhost:9090/students'
    response = requests.get(api_url)
    if response.status_code == 200:
        students = response.json()
        return render(request, 'listStudent.html',{"students": students})
    else:
        return render(request, 'error.html', {'message': 'Error al obtener datos'})

# def createStudent(request):
#     student = Students(dni=request.POST['dni'],nombre=request.POST['nombre'],apellido=request.POST['apellido'])
#     student.save()
#     return redirect('/students/')
@csrf_exempt
def createStudent(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        spring_boot_url = 'http://localhost:9090/students',    
        response = requests.post(spring_boot_url, data={'data': data})
        return JsonResponse({'response': response.json()}, status=response.status_code)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def deleteStudent(request, student_id):
    student = Students.objects.get(id=student_id)
    student.delete()
    return redirect('/students/')
