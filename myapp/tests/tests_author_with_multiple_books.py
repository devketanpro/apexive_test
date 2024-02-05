from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from myapp.models import Book, Author

class AuthorsWithMultipleBooksAPIViewTest(TestCase):
    def setUp(self):
        # Create test data (two authors, one with multiple books and one with a single book)
        self.author1 = Author.objects.create(name='Author1', email = "author1@gmail.com")
        self.author2 = Author.objects.create(name='Author2', email = "author2@gmail.com")

        self.book1 = Book.objects.create(title='Book1', author=self.author1, published_date='2023-01-01')
        self.book2 = Book.objects.create(title='Book2', author=self.author1, published_date='2023-01-01')
        self.book3 = Book.objects.create(title='Book3', author=self.author2, published_date='2023-01-01')

        self.url = '/authors-with-multiple-books/'
        self.client = APIClient()

    def test_authors_with_multiple_books_api(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure only one author returned with their books
        self.assertEqual(1, len(response.json()))

    def test_empty_case_authors_with_multiple_books_api(self):
        # Create a new author with a single book
        author3 = Author.objects.create(name='Author3', email = "author3@gmail.com")
        Book.objects.create(title='Book4', author=author3, published_date='2023-01-01')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Ensure that authors with only one book are not included in the response
        self.assertNotIn(author3.id, [author['id'] for author in response.data])
