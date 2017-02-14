from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Hits(models.Model):
    name = models.CharField(max_length=200)
    hits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True)  # set blank when first creating it, add 1 each time

class TopMovies(models.Model):
    Title = models.CharField(max_length=200)
    Rank = models.IntegerField(default=-1)
    Released = models.DateTimeField(auto_now_add=True, blank=True)
    Poster = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    Year = models.IntegerField(default=-1)
    Genre = models.CharField(max_length=200)
    Awards = models.CharField(max_length=200)
    imdbRating = models.FloatField(default=-1)
    gross_revenue = models.FloatField(default=-1)
    Actors = models.CharField(max_length=200, default = 'Fei Wang')
    Director = models.CharField(max_length=200, default = 'Fei Wang')
    Plot = models.CharField(max_length=500, default = 'Fei Wang\s story')

class Key(models.Model):
    Key = models.CharField(max_length=200)
