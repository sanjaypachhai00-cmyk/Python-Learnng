from django.shortcuts import render,redirect
from .forms import StudentForm


def all_students(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(
        request,
        'students/all_students.html',
        context
    )
from django.shortcuts import get_object_or_404
from .models import Student


def all_students(request):

    students = Student.objects.all()

    return render(
        request,
        'students/all_students.html',
        {'students': students}
    )


def student_detail(request, id):

    student = get_object_or_404(Student, id=id)

    return render(
        request,
        'students/student_detail.html',
        {'student': student}
    )
def main_page(request):

    return render(
        request,
        'students/main.html'
    )

def add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('all_students')

    else:

        form = StudentForm()

    return render(
        request,
        'students/add_student.html',
        {'form': form}
    )

    from django.shortcuts import render

def custom_404(request, exception):
    return render(
        request,
        '404.html',
        status=404
    )
from django.shortcuts import render

def student_list(request):

    name = "Sanjay"
    age = 22
    course = "Computer Engineering"

    return render(request, 'students/student_list.html', {
        'name': name,
        'age': age,
        'course': course
    })