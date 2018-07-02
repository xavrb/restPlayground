from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse



from .models import Movie

class ModelTestCase(TestCase):
    """This class defines the test suite for the movie  model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.title = "An epic movie lolololol"
        self.movie = Movie(title=self.title)

    def test_model_can_create_a_movie(self):
        """Test the movie model can create a movie."""
        old_count = Movie.objects.count()
        self.movie.save()
        new_count = Movie.objects.count()
        self.assertNotEqual(old_count, new_count)


# new tests for views



class ViewTestCase(TestCase):
    """ Test suite for the api views"""


    def setUp(self):
        """ Define the test client and other  test variables """
        self.client = APIClient()
        self.movie_data = {"title" : "a movie",
        "genre" : "Horror",
        "cast" : "someone",
        "director" : "GDT", 
        "year" : "3000",
        "country" : "MX", 
        "comment" : "a comment on this movie", 
        "rating" : 5
        }
        self.response = self.client.post(
            reverse('create'),
            self.movie_data,
            format="json")


    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
