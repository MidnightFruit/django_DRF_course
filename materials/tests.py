from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Lesson, Subscribe, Course

User = get_user_model()


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User( email='test@mail.com',
            first_name='Tester',
            last_name='Tester',
            )
        self.user.set_password('321')
        self.user.save()
        self.lessen = Lesson.objects.create(
            name="test1",
            description='tested',
            video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygULcmljayBhc3RsZXk%3D',
            owner=self.user
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        self.client.force_authenticate(user=self.user)

        data = {
            "name": 'test',
            'description': 'tested',
            'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygULcmljayBhc3RsZXk%3D'
        }
        response = self.client.post(
            '/material/create_lessons/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_retrieve_lesson(self):
        """Тестирование просмотра 1 урока"""
        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse('materials:retrieve_lessons', args=[self.lessen.id])
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_lesson(self):
        """Тестирование просмотра всех уроков"""
        self.client.force_authenticate(self.user)
        response = self.client.get(reverse('materials:lessons_list'))
        data = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'name': 'test1',
                    'description': 'tested',
                    'preview': None,
                    'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygULcmljayBhc3RsZXk%3D',
                    'course': None
                }
            ]
        }
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data,
            data
        )

    def test_update_lesson(self):
        """Тестирование изменения урока"""
        self.client.force_authenticate(user=self.user)

        response = self.client.patch(reverse('materials:update_lessons', args=[self.lessen.id]), {'name': 'test2'})

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(Lesson.objects.filter(name='test2').exists())



    def test_destroy_lesson(self):
        """Тестирование удаления урока"""
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse('materials:delete_lessons', args=[self.lessen.id]))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User( email='test@mail.com',
            first_name='Tester',
            last_name='Tester',
            )
        self.user.set_password('321')
        self.user.save()
        self.course = Course.objects.create(
            name='test',
            description='description',
            owner=self.user
        )

    def test_subs(self):
        self.client.force_authenticate(user=self.user)

        data = {'course': 1}
        response = self.client.post(reverse('materials:subs'), data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        response = self.client.post(reverse('materials:subs'), data=data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )