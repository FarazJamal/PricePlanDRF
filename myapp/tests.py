from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import App, Plan, Subscription
from .serializers import AppSerializer, PlanSerializer, SubscriptionSerializer

class AppViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_app(self):
        data = {'name': 'Test App', 'description': 'Test Description', 'user': self.user.id}
        response = self.client.post('/apiplan/apps/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_app(self):
        app = App.objects.create(name='Test App', description='Test Description', user=self.user)
        response = self.client.get(f'/apiplan/apps/{app.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_app(self):
        app = App.objects.create(name='Test App', description='Test Description', user=self.user)
        data = {'name': 'Updated App'}
        response = self.client.put(f'/apiplan/apps/{app.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_app(self):
        app = App.objects.create(name='Test App', description='Test Description', user=self.user)
        response = self.client.delete(f'/apiplan/apps/{app.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class PlanViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_plan(self):
        data = {'name': 'Test Plan', 'price': 'Free'}
        response = self.client.post('/apiplan/plans/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_plan(self):
        plan = Plan.objects.create(name='Test Plan', price='Free')
        response = self.client.get(f'/apiplan/plans/{plan.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_plan(self):
        plan = Plan.objects.create(name='Test Plan', price='Free')
        data = {'name': 'Updated Plan'}
        response = self.client.put(f'/apiplan/plans/{plan.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_plan(self):
        plan = Plan.objects.create(name='Test Plan', price='Free')
        response = self.client.delete(f'/apiplan/plans/{plan.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class SubscriptionViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.app = App.objects.create(name='Test App', description='Test Description', user=self.user)
        self.plan = Plan.objects.create(name='Test Plan', price='Free')

    def test_create_subscription(self):
        data = {'app': self.app.id, 'plan': self.plan.id, 'active': True}
        response = self.client.post('/apiplan/subscriptions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_subscription(self):
        subscription = Subscription.objects.create(app=self.app, plan=self.plan, active=True)
        response = self.client.get(f'/apiplan/subscriptions/{subscription.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_subscription(self):
        subscription = Subscription.objects.create(app=self.app, plan=self.plan, active=True)
        data = {'active': False}
        response = self.client.put(f'/apiplan/subscriptions/{subscription.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subscription(self):
        subscription = Subscription.objects.create(app=self.app, plan=self.plan, active=True)
        response = self.client.delete(f'/apiplan/subscriptions/{subscription.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
