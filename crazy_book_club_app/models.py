from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    ##description for a book
    #name of book
    name=models.CharField(max_length=400)
    #name of author
    authors=models.JSONField() 
    #publishing year for the book
    year_published=models.IntegerField()
    #date and time on which the model was created and modified.
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    #the person who created the class instance
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        ##returns the model for the book as a string.
        return f'{self.name}, {self.authors}, {self.year_published}, {self.date_added}'

class Review(models.Model):
    #Description for a review
    #Place to store review
    my_review=models.TextField()
    #place to store a star rating for a book
    stars=models.IntegerField()
    #check false if you have completed the book
    unfinished=models.BooleanField()
    #date and time for when the review was added and modified
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    #a variable to link the review to a book in the database
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    owner=3 #models.ForeignKey(User, on_delete=models.CASCADE)
    #meta field changes the name of the model into plural.
    class Meta:
        verbose_name_plural='Reviews'
 

    def __str__(self):
        #returns representation of the model Review.
        return f'Review for {self.book}'
