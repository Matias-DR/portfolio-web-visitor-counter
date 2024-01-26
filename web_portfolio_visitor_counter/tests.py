from rest_framework.test import APITestCase


class CounterViewTestCase(APITestCase):
    def setUp(self):
        self.data = {
            'ip': 'i.p.e.x'
        }

    def test_post(self):
        response = self.client.post(
            '/api/counter/',
            self.data,
            format='json'
        )
        print(response)
        self.assertEqual(response.status_code, 200)
