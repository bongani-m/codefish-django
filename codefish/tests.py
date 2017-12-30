from django.test import TestCase, Client
from django.contrib.auth.models import User

class CodefishTest(TestCase):
    def test_default_route_returns_hello_world(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello, World!')

    def test_login_page_render(self):
        response = self.client.get('/login/')
        self.assertContains(response, 'Login')

    def test_login_right(self):
        User.objects.create_user(username = 'test', email = 'test@test.com', password = 'test')
        c = Client()
        response = c.post('/login/', {
            'username': 'test',
            'password': 'iamnumber1'
        })
        self.assertEquals(response.status_code, 200)

    def test_login_wrong(self):
        User.objects.create_user(username = 'test', email = 'test@test.com', password = 'test')
        c = Client()
        response = c.post('/login/', {
            'username': 'test',
            'password': 'wrong'
        })
        self.assertContains(response, 'Username and Password combo does not match')

    def test_logout(self):
        user = User.objects.create_user(username = 'test', email = 'test@test.com', password = 'test')
        c = Client()
        response = c.post('/login/', {
            'username': 'test',
            'password': 'iamnumber1'
        })
        response = c.get('/logout/')
        self.assertEquals(response.status_code, 302)

    def test_protected_page_auth(self):
        self.client.login(username = 'admin', password = 'password')
        response = self.client.get('/protected', follow = True)
        self.assertEquals(response.status_code, 200)

    def test_protected_page_unauth(self):
        response = self.client.get('/protected')
        self.assertEquals(response.status_code, 302)