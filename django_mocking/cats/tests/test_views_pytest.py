import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_randomcat(client, mocker):
    mock_response = mocker.patch("requests.get")
    mock_response.status_code = 200
    mock_response.json_response = "{}"
    # Start the test.
    url = reverse("randomcat")
    response = client.get(url)
    assert response.status_code == 200
    print("json response", response.context[1]["json_response"])
