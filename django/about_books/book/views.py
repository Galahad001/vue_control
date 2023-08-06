from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import BooksSerializer

class APIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

# Create your views here.
