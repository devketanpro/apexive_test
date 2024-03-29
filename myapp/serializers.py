from datetime import date

from rest_framework import serializers

from myapp.models import (
    Author,
    Book,
)


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Book model.

    This serializer is responsible for converting Book model instances to
    JSON representations and vice versa. It utilizes the default ModelSerializer
    provided by Django REST framework, which automatically generates fields
    based on the Book model's attributes.
    """

    author_name = serializers.CharField(source="author.name", read_only=True)
    since_creation_in_days = serializers.SerializerMethodField(
        "get_since_creation_in_days"
    )

    class Meta:
        model = Book
        fields = (
            "title",
            "published_date",
            "author",
            "author_name",
            "since_creation_in_days",
        )

    def get_since_creation_in_days(self, obj: Book) -> str:
        days_since_creation = (date.today() - obj.published_date).days
        return days_since_creation


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer converts Author model instances to and from JSON
    representation. It includes a nested serialization of associated Book
    objects using the BookSerializer.

    Attributes:
        - books (BookSerializer): Nested serializer for handling Book objects
          associated with the author. This is read-only and is used for
          serialization purposes.

    Meta:
        model (Author): The model class that this serializer is associated
          with.
        fields (str): The fields to include in the serialized representation.
          Here, "__all__" indicates that all fields from the Author model
          should be included.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = "__all__"
