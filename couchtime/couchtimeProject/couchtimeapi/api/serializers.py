from rest_framework import serializers  
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """ Meta class to map serializers' fields with the model fields """
        model = Movie
        fields = ('id',
        'title',
        'genre',
        'cast',
        'director',
        'year',
        'country',
        'comment',
        'rating',
        'created_at'
        )
        read_only_fields = ('created_at',)
