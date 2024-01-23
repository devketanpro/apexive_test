from datetime import date
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from myapp.models import Author, Book
from myapp.serializers import BookSerializer

class BookViewSetTestCase(TestCase):
    def setUp(self):
        # Create some sample data for testing
        self.author = Author.objects.create(name='Author1', email='author1@example.com')
        self.book = Book.objects.create(title='Book1', published_date=date.today(), author=self.author)
        self.client = APIClient()

    def test_list_books(self):
        # Test GET request to list all books
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Book.objects.count())

    def test_retrieve_book(self):
        # Test GET request to retrieve a specific book
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['author_name'], self.book.author.name)

    def test_create_book(self):
        # Test POST request to create a new book
        data = {'title': 'New Book', 'published_date': '2023-01-01', 'author': self.author.id}
        url = reverse('book-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.filter(title='New Book').exists(), True)

    def test_update_book(self):
        # Test PUT request to update an existing book
        data = {'title': 'Updated Book', 'published_date': '2022-01-01', 'author': self.author.id}
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, 'Updated Book')

    def test_delete_book(self):
        # Test DELETE request to delete an existing book
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.filter(id=self.book.id).exists(), False)


class BookSerializerTestCase(TestCase):
    def setUp(self):
        # Create some sample data for testing
        self.author = Author.objects.create(name='Author1', email='author1@example.com')
        self.book = Book.objects.create(title='Book1', published_date=date.today(), author=self.author)

    def test_book_serializer_fields(self):
        # Test if the serializer fields are correctly generated
        serializer = BookSerializer(instance=self.book)
        expected_fields = ['title', 'published_date', 'author', 'author_name', 'since_creation_in_days']
        self.assertEqual(set(serializer.data.keys()), set(expected_fields))

    def test_since_creation_in_days_calculation(self):
        # Test the 'since_creation_in_days' calculation in the serializer
        serializer = BookSerializer(instance=self.book)
        days_since_creation = (date.today() - self.book.published_date).days
        self.assertEqual(serializer.data['since_creation_in_days'], days_since_creation)
