from django.test import TestCase

# Create your tests here.


from .models import Movie

class ModelTestCase(TestCase):
    """This class defines the test suite for the movie  model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.movie_name = "Write world class code"
        self.movie = Movie(name=self.movie_name)

    def test_model_can_create_a_movie(self):
        """Test the movie model can create a movie."""
        old_count = Movie.objects.count()
        self.movie.save()
        new_count = Movie.objects.count()
        self.assertNotEqual(old_count, new_count)
