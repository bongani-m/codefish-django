from django.test import TestCase, Client

class CodefishTest(TestCase):
    def test_default_route_returns_hello_world(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello, World!')

    def test_login_page_render(self):
        response = self.client.get('/login/')
        self.assertContains(response, 'Login')

    def test_login(self):
        c = Client()
        response = c.post('/login/', {'username': 'admin', 'password': 'iamnumber1'})
        self.assertEquals(response.status_code, 200)

    def test_protected_page_auth(self):
        self.client.login(username='admin', password='password')
        response = self.client.get('/protected', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_protected_page_unauth(self):
        response = self.client.get('/protected')
        self.assertEquals(response.status_code, 302)