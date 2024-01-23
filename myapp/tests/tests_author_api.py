from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from myapp.models import Author
from myapp.serializers import AuthorSerializer

class AuthorViewSetTestCase(TestCase):
    def setUp(self):
        # Create some sample data for testing
        self.author1 = Author.objects.create(name='Author1', email='author1@example.com')
        self.author2 = Author.objects.create(name='Author2', email='author2@example.com')
        self.client = APIClient()

    def test_list_authors(self):
        # Test GET request to list all authors
        url = reverse('author-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Author.objects.count())

    def test_retrieve_author(self):
        # Test GET request to retrieve a specific author
        url = reverse('author-detail', args=[self.author1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.author1.name)
        self.assertEqual(response.data['email'], self.author1.email)

    def test_create_author(self):
        # Test POST request to create a new author
        data = {'name': 'New Author', 'email': 'new_author@example.com'}
        url = reverse('author-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.filter(name='New Author').exists(), True)

    def test_update_author(self):
        # Test PUT request to update an existing author
        data = {'name': 'Updated Author', 'email': 'updated_author@example.com'}
        url = reverse('author-detail', args=[self.author1.id])
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get(id=self.author1.id).name, 'Updated Author')

    def test_delete_author(self):
        # Test DELETE request to delete an existing author
        url = reverse('author-detail', args=[self.author1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.filter(id=self.author1.id).exists(), False)
