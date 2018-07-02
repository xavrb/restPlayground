from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=300, default = "title")
    genre = models.CharField(max_length=100,default = "none")
    cast = models.CharField(max_length=500,default = "none")
    director = models.CharField(max_length=50,default = "none")
    year = models.CharField(max_length=4,default = "none")
    country = models.CharField(max_length=20,default = "none")
    comment = models.CharField(max_length=1000,default = "no comment")
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)




def __str__(self):
    return '%s %s %s %s %s %s %s %d' % (
        self.title,
        self.genre,
        self.cast,
        self.director,
        self.year,
        self.country,
        self.comment,
        self.rating,
        self.created_at
    )
