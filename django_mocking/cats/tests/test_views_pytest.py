import pytest

from django.urls import reverse

pytestmark = pytest.mark.django_db

def test_randomcat(client):
    url = reverse('randomcat')
    response = client.get(url)
    assert response.status_code == 200
    print('json response', response.context[1]['json_response'])
