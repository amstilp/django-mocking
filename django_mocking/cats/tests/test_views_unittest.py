from unittest import mock

from django.test import TestCase
from django.urls import reverse


class RandomCatTest(TestCase):
    """Unit tests for RandomCat view"""

    @mock.patch("requests.get")
    def test_view(self, mock_response):
        # Set up mock request
        mock_response.return_value.status_code = 200
        mock_response.json.return_value = {"test": "test2"}
        # Start the test.
        response = self.client.get(reverse("randomcat"))
        self.assertEqual(response.status_code, 200)
        print("json response", response.context[1]["json_response"])
