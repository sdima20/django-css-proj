from django.test import TestCase

from .models import Course

from unittest.mock import patch

# Create your tests here.
class BasicTest(TestCase):

    def test_math(self):
        self.assertEqual(2 + 2, 4)

class CourseModelTest(TestCase):

    def test_create_course(self):
        course = Course.objects.create(title='Python', price=100)

        self.assertEqual(course.title, 'Python')
    
    def test_count_courses(self):

        Course.objects.create(title='Python', price=100)
        Course.objects.create(title='SQL', price=50)

        count = Course.objects.count()
        self.assertEqual(count, 2)


class CoursesViewTest(TestCase):

    def test_courses_page(self):
        response = self.client.get('/courses/')

        self.assertEqual(response.status_code, 200)
    
    def test_page_contains_course(self):
        Course.objects.create(title='Python Frameworks', price=100)

        response = self.client.get('/courses/')

        self.assertContains(response, "Python Frameworks")

class CreateCourseTest(TestCase):

    def test_create_course_post(self):

        response = self.client.post('/create/',{
            'title' : 'Django',
            'price' : 200
        })

        count = Course.objects.count()
        self.assertEqual(count, 1)

class ApiTest(TestCase):

    def test_api(self):
        Course.objects.create(title='Python', price=200)

        response = self.client.get('/api/')

        self.assertEqual(response.status_code, 200)


class MockTest(TestCase):
    @patch('courses.views.send_email')
    def test_mock_email(self, mock_send):

        mock_send.return_value = True

        self.client.post('/create/', {
            'title':'SQL', 
            'price':100
            })

        mock_send.assert_called_once()