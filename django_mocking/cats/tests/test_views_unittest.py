from unittest import mock

from django.test import RequestFactory, TestCase
from django.urls import reverse

from django_mocking.cats.views import RandomCat

class RandomCatTest(TestCase):
    """Unit tests for RandomCat view"""

    @mock.patch("requests.get")
    def test_view_with_client(self, mock_response):
        # Set up mock request
        mock_response.return_value.status_code = 200
        mock_response.json.return_value = {"test": "test2"}
        # Start the test.
        response = self.client.get(reverse("randomcat"))
        self.assertEqual(response.status_code, 200)
        print("json response", response.context[1]["json_response"])

    @mock.patch("requests.get")
    def test_view_with_request_factory(self, mock_response):
        # Set up mock request
        mock_response.return_value.status_code = 200
        mock_response.json.return_value = {"test": "test2"}
        # Start the test.
        request = RequestFactory().get(reverse("randomcat"))
        response = RandomCat.as_view()(request)
        self.assertEqual(response.status_code, 200)
        print("json response", response.context_data['json_response'])
