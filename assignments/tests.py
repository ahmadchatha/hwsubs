from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group


class AssignmentsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.class1 = Group.objects.create(name='class1')
        self.class2 = Group.objects.create(name='class2')
        self.admin = User.objects.create_superuser(username='admin', email='admin@a.com', password='QWE123qwe')
        self.student1 = User.objects.create_user(username='s1', email='s1@a.com', password='QWE123qwe1')
        self.student1.groups.add(self.class1)
        self.student2 = User.objects.create_user(username='s2', email='s2@a.com', password='QWE123qwe2')
        self.student1.groups.add(self.class2)

    def testCreate(self):
        self.client.force_authenticate(user=self.admin)
        data = {'name': 'new assignment',
                'group': 'http://testserver' + reverse('group-list') + str(self.class1.id) + '/',
                'description': 'test'}
        response = self.client.post('/assignments/', data, format='json')
        self.assertEqual(response.status_code, 201)

        self.client.force_authenticate(user=self.student1)
        response = self.client.post('/assignment/', data, format='json')
        self.assertEqual(response.status_code, 404)

    def testList(self):
        self.client.force_authenticate(user=self.admin)
        data = {'name': 'new assignment',
                'group': 'http://testserver' + reverse('group-list') + str(self.class1.id) + '/',
                'description': 'test'}
        self.client.post('/assignments/', data, format='json')
        data['name'] = 'brand new assignment'
        self.client.post('/assignments/', data, format='json')

        response = self.client.get('/assignments/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 2)

        self.client.force_authenticate(user=self.student1)
        response = self.client.get('/assignments/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 2)

        self.client.force_authenticate(user=self.student2)
        response = self.client.get('/assignments/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 0)