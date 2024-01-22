from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r"author", AuthorViewSet, basename="author"),
router.register(r"books", BookViewSet, basename="book")

urlpatterns = [
    path("", include(router.urls)),
]
