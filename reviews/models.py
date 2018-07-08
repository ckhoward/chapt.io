from django.db import models
from django.conf import settings
from django.urls import reverse
from django.forms import ModelForm
from django import forms


RATING_CHOICES = (
        ('Boring', 'Boring'),
        ('Engaging', 'Engaging')
    )

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])



class Book(models.Model):   
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])



class Chapter(models.Model):
    chapter_number = models.PositiveIntegerField(default=0)   
    title = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "Chapter " + str(self.chapter_number) + ": " + self.title

    def get_absolute_url(self):
        return reverse('chapter_detail', args=[str(self.id)])

    #Functions to get rating counts for book_detail column charts
    def engaging_reviews_count(self):
        return self.rating_set.filter(review='Engaging').count()

    def boring_reviews_count(self):
        return self.rating_set.filter(review='Boring').count()

  

class Rating(models.Model):
    review = models.CharField(max_length=15, choices=RATING_CHOICES, blank=False)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.review







