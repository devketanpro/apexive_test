from django.db import models


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
        return self.filter(published_date__gt=date)


class BookManager(models.Manager):
    """
    Custom manager for the Book model.

    This manager enhances the default queryset capabilities by using a custom
    queryset class called BookQuerySet. It provides additional methods for
    querying and filtering Book objects.

    Methods:
        - published_after(date): Returns a queryset of books published after
          the specified date.

    Usage example:
    ```
    # Get books published after a specific date
    recent_books = Book.objects.published_after(some_date)
    ```
    """

    def get_queryset(self):
        """
        Returns a queryset using the custom BookQuerySet.
        """

        return BookQuerySet(self.model, using=self._db)

    def published_after(self, date):
        """
        Returns a queryset of books published after the specified date.
        """

        return self.get_queryset().published_after(date)


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

    def __str__(self):
        """
        Returns a string representation of the book, using its title.
        """
        return self.title
