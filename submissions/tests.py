from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group


class SubmissionTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.class1 = Group.objects.create(name='class1')
        self.class2 = Group.objects.create(name='class2')
        self.admin = User.objects.create_superuser(username='admin', email='admin@a.com', password='QWE123qwe')
        self.student1 = User.objects.create_user(username='s1', email='s1@a.com', password='QWE123qwe1')
        self.student1.groups.add(self.class1)
        self.student2 = User.objects.create_user(username='s2', email='s2@a.com', password='QWE123qwe2')
        self.student1.groups.add(self.class2)

        self.client.force_authenticate(user=self.admin)
        data = {'name': 'new assignment',
                'group': 'http://testserver' + reverse('group-list') + str(self.class1.id) + '/',
                'description': 'test'}
        res = self.client.post('/assignments/', data, format='json')
        self.assertEqual(res.status_code, 201)
        self.assignment = res.json()

    def testCreate(self):
        self.client.force_authenticate(user=self.student1)
        data = {'assignment': 'http://testserver' + reverse('assignment-list') + str(self.assignment['id']) + '/',
                'link': 'https://www.test.com'}
        response = self.client.post('/submissions/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def testList(self):
        self.client.force_authenticate(user=self.student1)
        data = {'assignment': 'http://testserver' + reverse('assignment-list') + str(self.assignment['id']) + '/',
                'link': 'https://www.test.com'}
        response = self.client.post('/submissions/', data, format='json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/submissions/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)

        self.client.force_authenticate(user=self.student2)
        response = self.client.get('/submissions/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 0)