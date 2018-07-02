from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializer
from .models import Movie



# Create your views here.


class CreateView(generics.ListCreateAPIView):
    """ This class defines the create behavior of our rest api """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

    def perform_create(self, serializer):
        """Save the post data when creating a new movie """
        

        serializer.save()
