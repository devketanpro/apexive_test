from rest_framework import viewsets

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
