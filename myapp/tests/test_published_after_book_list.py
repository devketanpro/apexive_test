from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from myapp.models import Author, Book

class PublishedAfterBookListTestCase(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name='Author1', email = "author1@gmail.com")
        # Create some sample books for testing
        Book.objects.create(title='Book 1', author=self.author1, published_date='2022-01-01')
        Book.objects.create(title='Book 2', author=self.author1, published_date='2022-02-01')
        Book.objects.create(title='Book 3', author=self.author1, published_date='2023-01-01')

    def test_published_after_book_list(self):
        # Set up the client
        client = APIClient()

        # Define the date parameter for the test
        date = '2022-12-01'

        # Make a GET request to the API endpoint
        url = reverse('published-after-book-list', kwargs={'date': date})
        response = client.get(url)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the response data matches the only one books match this criteria
        self.assertEqual(len(response.json()), 1)
