from django.test import TestCase

class CodefishTest(TestCase):
    def test_default_route_returns_hello_world(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello, World!')

