import pytest
from django.urls import reverse
from rest_framework import status

from ..models import Picture


@pytest.mark.django_db
def test_allowed_only_for_authorized_clients(client):
    url = reverse('api:app:image-list')

    response = client.get(url)

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_user_can_access_only_itself_pictures(client, django_user_model):
    user = django_user_model.objects.create(
        username='user',
        password='password'
    )
    picture = Picture.objects.create(title='user picture', owner=user)
    url = reverse('api:app:image-list')
    data = [
        {
            "title": picture.title,
            "image": None,
            "owner": user.pk
        },
    ]

    client.force_login(user)
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == data


@pytest.mark.django_db
def test_admin_can_access_all_pictures(client, django_user_model):
    admin = django_user_model.objects.create(
        username='admin',
        password='password',
        is_superuser=True,
    )
    user = django_user_model.objects.create(
        username='user',
        password='password'
    )
    admin_picture = Picture.objects.create(title='admin picture', owner=admin)
    user_picture = Picture.objects.create(title='user picture', owner=user)
    url = reverse('api:app:image-list')
    data = [
        {
            "title": admin_picture.title,
            "image": None,
            "owner": admin.pk
        },
        {
            "title": user_picture.title,
            "image": None,
            "owner": user.pk
        },
    ]

    client.force_login(admin)
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == data
