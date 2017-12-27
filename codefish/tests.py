from django.test import TestCase

class CodefishTest(TestCase):
    def test_entered_the_codeship(self):
        response = self.client.get('/')
        self.assertContains(response, "I've entered the Codeship")
    
    def test_leads_to_the_codeship(self):
        response = self.client.get('/')
        self.assertContains(response, '<a href="https://www.codeship.io">')

    def test_that_says_hello_world(self):
        response = self.client.get('hello/')
        self.assertContains(response, 'Hello, World!')
