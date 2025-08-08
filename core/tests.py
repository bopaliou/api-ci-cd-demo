from django.test import SimpleTestCase
from django.urls import reverse

class PingTestCase(SimpleTestCase):
    def test_ping(self):
        response = self.client.get('/api/ping/')
        print("Response code:", response.status_code)
        print("Response content:", response.content)
        self.assertEqual(response.status_code, 200)
