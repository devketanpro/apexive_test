from rest_framework import viewsets, generics

from myapp.models import Author, Book
from myapp.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for interacting with Author objects.

    This ViewSet provides CRUD (Create, Retrieve, Update, Delete) operations
    for Author objects. It is backed by the Author model and uses the
    AuthorSerializer for serialization.

    Attributes:
        queryset (QuerySet): The default queryset containing all Author objects.
        serializer_class (Serializer): The serializer class used for
            serialization and deserialization of Author objects.
    Usage example:
    ```
    # To retrieve a list of all authors
    GET /authors/

    # To retrieve details of a specific author
    GET /authors/{author_id}/

    # To create a new author
    POST /authors/

    # To update an existing author
    PUT /authors/{author_id}/

    # To delete an author
    DELETE /authors/{author_id}/
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API ViewSet for managing Book objects.

    This ViewSet provides CRUD (Create, Retrieve, Update, Delete) operations
    for Book objects through the Book model. It utilizes the default Django
    queryset and a specified serializer class for data representation.

    Attributes:
        - queryset (QuerySet): The default queryset for retrieving Book objects.
        - serializer_class (Serializer): The serializer class for converting
          Book objects to/from JSON.

    Usage example:
    ```
    # Retrieve a list of all books
    GET /api/books/

    # Retrieve details of a specific book
    GET /api/books/{book_id}/

    # Create a new book
    POST /api/books/

    # Update an existing book
    PUT /api/books/{book_id}/

    # Delete a book
    DELETE /api/books/{book_id}/
    ```
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PublishedAfterBookList(generics.ListAPIView):
    """
    A DRF API endpoint that returns a list of books published after a specified date.

    Parameters:
    - `date` (str): The date in the format 'YYYY-MM-DD'. Books published after this date will be included.

    Example Usage:
    ```
    GET /books/published_after/2023-01-01/
    ```
    Serializer:
    - Uses `BookSerializer` for serializing the book objects.

    View:
    - Inherits from DRF's `generics.ListAPIView`.
    - Overrides the `get_queryset` method to filter books based on the provided date.

    Note: The `published_after` method is assumed to be a custom manager method in the Book model.

    """

    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Get a queryset of books published after the specified date.

        Returns:
        - Queryset of books meeting the criteria.
        """

        date = self.kwargs['date']
        return Book.objects.published_after(date)
    

class AuthorsWithMultipleBooksAPIView(generics.ListAPIView):
    """
    API endpoint to retrieve a list of authors with multiple books.

    This endpoint returns a list of authors who have written more than one book.

    ## Response
    - HTTP 200 OK: Returns a list of authors with their details.

    ### Serializer
    - `AuthorSerializer`: Serializes Author instances.

    ### Method
    - `GET`: Retrieves a list of authors with multiple books.

    ### Query Parameters
    - No specific query parameters are required.

    ## Example Usage
    ```bash
    curl -X GET http://localhost:8000/authors-with-multiple-books/
    ```
    """

    serializer_class = AuthorSerializer

    def get_queryset(self):
        """
        Get the queryset of authors with multiple books.

        Returns:
        - Queryset of authors with multiple books.
        """
        return Book.objects.authors_with_multiple_books()
    