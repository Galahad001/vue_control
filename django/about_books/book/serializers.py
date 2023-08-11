from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'content', 'author', 'path_to_photo', 'the_year_of_publishing', 'time_create', 'time_update', 'visibility', 'index', 'pk', 'id', 'cat')