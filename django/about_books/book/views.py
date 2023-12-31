from django.shortcuts import render
# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import BooksSerializer

@api_view(['GET', 'POST'])
def APIView(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # queryset = Books.objects.all()
    # serializer_class = BooksSerializer


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def APIView_datail(request, pk):
    
    try:
        book = Books.objects.get(pk=pk)

    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BooksSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = BooksSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.
