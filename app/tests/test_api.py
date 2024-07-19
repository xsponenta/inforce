import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import User
from restaurants.models import Restaurant, Menu
from employees.models import Employee, Vote
from datetime import date

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_data():
    return {'username': 'testuser', 'password': 'testpass123'}

@pytest.fixture
def authenticated_client(api_client, user_data):
    user = User.objects.create_user(**user_data)
    api_client.force_authenticate(user=user)
    return api_client

@pytest.mark.django_db
def test_user_registration(api_client, user_data):
    url = reverse('register')
    response = api_client.post(url, user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert User.objects.get().username == 'testuser'

@pytest.mark.django_db
def test_token_obtain(api_client, user_data):
    User.objects.create_user(**user_data)
    url = reverse('token_obtain_pair')
    response = api_client.post(url, user_data)
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data

@pytest.mark.django_db
def test_create_restaurant(authenticated_client):
    url = reverse('create_restaurant')
    data = {'name': 'Test Restaurant'}
    response = authenticated_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Restaurant.objects.count() == 1
    assert Restaurant.objects.get().name == 'Test Restaurant'

@pytest.mark.django_db
def test_upload_menu(authenticated_client):
    user = User.objects.get()
    restaurant = Restaurant.objects.create(user=user, name='Test Restaurant')
    url = reverse('upload_menu')
    data = {
        'date': str(date.today()),
        'items': {'dish1': 'Pizza', 'dish2': 'Salad'}
    }
    response = authenticated_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Menu.objects.count() == 1
    assert Menu.objects.get().items == data['items']

@pytest.mark.django_db
def test_create_employee(authenticated_client):
    url = reverse('create_employee')
    response = authenticated_client.post(url)
    assert response.status_code == status.HTTP_201_CREATED
    assert Employee.objects.count() == 1
    assert Employee.objects.get().user == User.objects.get()

@pytest.mark.django_db
def test_vote(authenticated_client):
    user = User.objects.get()
    employee = Employee.objects.create(user=user)
    restaurant = Restaurant.objects.create(user=user, name='Test Restaurant')
    menu = Menu.objects.create(
        restaurant=restaurant,
        date=date.today(),
        items={'dish1': 'Pizza', 'dish2': 'Salad'}
    )
    url = reverse('vote')
    data = {'menu': menu.id}
    response = authenticated_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Vote.objects.count() == 1
    assert Vote.objects.get().menu == menu

@pytest.mark.django_db
def test_get_results(authenticated_client):
    url = reverse('get_results')
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK