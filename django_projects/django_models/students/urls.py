from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.all_students, name='all_students'),
    


    path(
        'students/',
        views.all_students,
        name='all_students'
    ),

    path(
        'students/<int:id>/',
        views.student_detail,
        name='student_detail'
    ),



    path('', views.main_page, name='main'),

    path(
    'students/add/',
    views.add_student,
    name='add_student'
),
]

