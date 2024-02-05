from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import AuthorViewSet, BookViewSet, PublishedAfterBookList, AuthorsWithMultipleBooksAPIView

router = DefaultRouter()
router.register(r"author", AuthorViewSet, basename="author"),
router.register(r"books", BookViewSet, basename="book")

urlpatterns = [
    path("", include(router.urls)),
    path('authors-with-multiple-books/', AuthorsWithMultipleBooksAPIView.as_view(), name='authors_with_multiple_books_api'),
    path('books-published-after/<str:date>/', PublishedAfterBookList.as_view(), name='published-after-book-list'),
]
