
from django.test import TestCase
from .models import Student


class StudentModelTest(TestCase):

    def test_create_student(self):

        student = Student.objects.create(
            name='Sanjay',
            email='sanjay@example.com',
            age=22,
            course='Computer Engineering'
        )

        self.assertEqual(student.name, 'Sanjay')
        self.assertEqual(student.age, 22)


class MainPageTest(TestCase):

    def test_main_page_status(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)


class StudentListTest(TestCase):

    def test_students_page(self):

        response = self.client.get('/students/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'students/all_students.html'
        )


class StudentDetailTest(TestCase):

    def setUp(self):

        self.student = Student.objects.create(
            name='Alex',
            email='alex@example.com',
            age=21,
            course='Computer Engineering'
        )

    def test_student_detail(self):

        response = self.client.get(
            f'/students/{self.student.id}/'
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alex')

    def test_invalid_student(self):

        response = self.client.get('/students/9999/')

        self.assertEqual(response.status_code, 404)
