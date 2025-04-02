# views.py

from rest_framework import viewsets

from rest_framework.response import Response

from .models import Book


class BookViewSet(viewsets.ViewSet):

    def list(self, request):

        books = Book.objects.all()

        data = []

        for book in books:

            data.append({

                "id": book.id,

                "title": book.title,

                "author": book.author.name,

                "published_date": book.publish_date

            })

        return Response(data)
