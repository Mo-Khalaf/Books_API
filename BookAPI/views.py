from .models import *
from .serializers import *
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import filters
from django.db import connection


class BookViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        data = [request.data['title'], request.data['description'], request.data['price'], request.data['rent_fee'],
                request.data['release_year'], request.data['author_id'], request.data['quantity'],
                request.data['category']]
        try:
            with connection.cursor() as cursor:
                cursor.callproc("create_book", data)
            return Response({'success': 'Book created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.callproc("index_books")
                result = cursor.fetchall()
                book_result = [
                    {"id": book[0], "title": book[1], "description": book[2], "price": book[3], "rent_fee": book[4],
                     "release_year": book[5], "author_id": book[6], "quantity": book[7], "category": book[8]} for book
                    in result]
            return Response({'success': 'Books fetched successfully', "data": book_result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.callproc("get_book_by_id", [kwargs['pk']])
                result = cursor.fetchall()
                book_result = [
                    {"id": book[0], "title": book[1], "description": book[2], "price": book[3], "rent_fee": book[4],
                     "release_year": book[5], "author_id": book[6], "quantity": book[7], "category": book[8]} for book
                    in result]
            return Response({'success': 'Book fetched successfully', "data": book_result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = [kwargs['pk'], request.data['title'], request.data['description'], request.data['price'],
                request.data['rent_fee'],
                request.data['release_year'], request.data['author_id'], request.data['quantity'],
                request.data['category']]
        try:
            with connection.cursor() as cursor:
                cursor.callproc("update_book", data)
            return Response({'success': 'Book updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            with connection.cursor() as cursor:
                cursor.callproc("remove_book_by_id", [kwargs['pk']])
            return Response({'success': 'Book deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

