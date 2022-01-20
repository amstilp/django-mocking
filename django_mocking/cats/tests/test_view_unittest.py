from django.test import TestCase
from django.urls import reverse


class RandomCatTest(TestCase):
    """Unit tests for RandomCat view"""

    def test_view(self):
        response = self.client.get(reverse('randomcat'))
        self.assertEqual(response.status_code, 200)
        print('json response', response.context[1]['json_response'])
