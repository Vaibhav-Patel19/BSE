from django.test import TestCase

#tests_views
class URLTests(TestCase):
    def test_checkLandingPage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_checkRegistrationPage(self):
        response = self.client.get('/registration/')
        self.assertEqual(response.status_code, 200)


    def test_checkLoginPage(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)