from django.db import models

class Book(models.Model):
    ##description for a book
    #name of book
    name=models.CharField(max_length=400)
    #name of author
    authors=models.JSONField() #jsonfield.JSONField() vai models.JSONField()?
    #publishing year for the book
    year_published=models.IntegerField()
    #date and time on which the model was created and modified.
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        ##returns the model for the book as a string.
        return f'Name:{self.name} \n Author:{self.authors} \n Year published:{self.year_published} \n Date added:{self.date_added} \n Date modified:{date_modified}'

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
    book=models.ForeignKey(Book)
    #I didn't find any meta fields that would be useful for this model.

    def __str__(self):
        return f'{self.my_review}, {self.stars}, {self.unfinished}, {self.date_added}'
