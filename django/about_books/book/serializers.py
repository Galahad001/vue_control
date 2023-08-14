from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'content', 'author', 'path_to_photo', 'time_create', 'id', 'cat')