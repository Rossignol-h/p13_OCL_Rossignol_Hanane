import pytest
from django.urls import reverse

# ====================================================== TEST HOME PAGE VIEW


@pytest.mark.django_db
def test_home(client):
    url = reverse('home')
    response = client.get(url)

    assert response.status_code == 200
    assert b"<title>Holiday Homes</title>" in response.content
