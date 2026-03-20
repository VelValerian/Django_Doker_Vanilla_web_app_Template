import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_page_status_code(client):
    """
    Integration test for the Home page.
    Verifies that the page loads correctly (200 OK).
    """
    url = reverse('pages:home')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_page_content(client):
    """
    Integration test to check elements of the template.
    Verifies that the home page contains expected SEO/Meta tags.
    """
    url = reverse('pages:home')
    response = client.get(url)
    # Check that the site title from our OG tags update is present
    assert "Nomondays | Creative Studio" in response.content.decode()
