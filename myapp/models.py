from django.db import models
from django.db.models import  Subquery, Count


class Author(models.Model):
    """
    Model representing an author.

    Attributes:
        name (str): The name of the author (up to 100 characters).
        email (str): The email address of the author (must be unique).

    Methods:
        __str__(): Returns the string representation of the author, which is the author's name.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        """
        String representation of the Author object.
        """

        return self.name


class BookQuerySet(models.QuerySet):
    """
    Custom queryset for the Book model.

    This queryset provides additional methods for filtering and querying Book objects.

    Example:
    ```python
    # Usage of the published_after method
    books = Book.objects.published_after(date(2022, 1, 1))
    ```
    """

    def published_after(self, date):
        """
        Returns a queryset of books who have published after the given date.
        """
        return self.filter(published_date__gt=date)
    
    def authors_with_multiple_books(self):
        """
        Returns a queryset of authors who have written multiple books.
        """
        subquery = (
            self.values('author')
            .annotate(book_count=Count('author'))
            .filter(book_count__gt=1)
            .values('author')
        )

        return Author.objects.filter(pk__in=Subquery(subquery))

class Book(models.Model):
    """
    Represents a book in the database.

    Attributes:
        title (str): The title of the book, with a maximum length of 200 characters.
        published_date (Date): The date when the book was published.
        author (Author): The author of the book, linked via a ForeignKey relationship to the Author model.

    Methods:
        __str__(): Returns a string representation of the book, using its title.

    Relationships:
        Each book is associated with an author through a ForeignKey relationship.
    """

    title = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    objects = BookQuerySet.as_manager()

    def __str__(self):
        """
        Returns a string representation of the book, using its title.
        """
        return self.title
