from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test_account@net.com',
            'password1': 'khali_69420',
            'password2': 'khali_69420'
        })
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username='testuser').exists())


class UserLoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='khali_69420')

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'khali_69420'
        })
        self.assertEqual(response.status_code, 302)  # Assuming redirect on success
        self.assertTrue('_auth_user_id' in self.client.session)
        
class UserLogoutTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='khali_69420')
        self.client.login(username='testuser', password='khali_69420')

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Assuming redirect on success
        self.assertFalse('_auth_user_id' in self.client.session)