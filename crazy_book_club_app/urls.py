'''defines URL patterns for crazy_book_club_app'''
from django.contrib import admin
from django.urls import URLPattern, path 
from . import views 

app_name='crazy_book_club_app'
urlpatterns= [ 
    #home page
    path('', views.index, name='index'),
    #page that shows all books
    path('booknames/', views.booknames, name='booknames'),
    #page for each book
    path('booknames/<int:bookname_id>/', views.bookname, name='bookname'),
    #page for adding new review
    path('new_book/', views.new_book, name='new_book'),
    #page for adding new review
    path('new_review/<int:bookname_id>/', views.new_review, name='new_review'),
    #page for editing reviews
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
]