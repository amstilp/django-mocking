from unittest import mock

from django.test import RequestFactory, TestCase
from django.urls import reverse

from django_mocking.cats.views import RandomCat

class RandomCatWithDecoratorTest(TestCase):
    """Unit tests for RandomCat view using a decorator for mocking."""

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


class RandomCatWithSetupPatchTest(TestCase):
    """Unit tests for RandomCat view using a setUp class for mocking."""

    def setUp(self):
        patcher = mock.patch('requests.get')
        self.mock_get = patcher.start()
        self.addCleanup(patcher.stop)

    def test_view_with_client(self):
        # Set up mock request
        self.mock_get.return_value.status_code = 200
        self.mock_get.json.return_value = {"test": "test2"}
        # Start the test.
        response = self.client.get(reverse("randomcat"))
        self.assertEqual(response.status_code, 200)
        print("json response", response.context[1]["json_response"])

    def test_view_with_request_factory(self):
        # Set up mock request
        self.mock_get.return_value.status_code = 200
        self.mock_get.json.return_value = {"test": "test3"}
        # Start the test.
        request = RequestFactory().get(reverse("randomcat"))
        response = RandomCat.as_view()(request)
        self.assertEqual(response.status_code, 200)
        print("json response", response.context_data['json_response'])
