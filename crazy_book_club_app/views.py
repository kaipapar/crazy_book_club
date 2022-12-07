from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Book, Review
from .forms import BookForm, ReviewForm
# Create your views here.

def index(request):
    '''the home page for crazy book club app'''
    return render(request,'crazy_book_club_app/index.html')

@login_required
def booknames(request):
    '''show all booknames'''
    booknames=Book.objects.filter(owner=request.user).order_by('date_added')
    context= {'booknames':booknames}
    return render(request, 'crazy_book_club_app/booknames.html', context)

@login_required   
def bookname(request, bookname_id):
    '''shows a single book and its reviews'''
    bookname=Book.objects.get(id=bookname_id)
    #assuring the bookname belongs to the correct user
    if bookname.owner!=request.user:
        raise Http404
    reviews=bookname.review_set.order_by('-date_added')
    context={'bookname':bookname, 'reviews':reviews}
    return render(request, 'crazy_book_club_app/bookname.html',context)

@login_required
def new_book(request):
    '''adds a new book'''
    if request.method != 'POST':
        #no data submitted--> create blank form
        form=BookForm()
    else:
        #POST data submitted --> process data
        form=BookForm(data=request.POST)
        if form.is_valid():
            new_book=form.save(commit=False)
            new_book.owner=request.user
            new_book.save()
            return redirect('crazy_book_club_app:booknames')
        #display a blank or invalid form:
    context={'form':form}
    return render(request,'crazy_book_club_app/new_book.html',context)

@login_required
def new_review(request, bookname_id):
    '''add a new review for a certain book'''
    review=Book.objects.get(id=bookname_id)
    if request.method!='POST':
        #no data submitted -> create blank form
        form=ReviewForm()
    else:
        #post the submitted data->process data
        form=ReviewForm(data=request.POST)
        if form.is_valid():
            new_review=form.save(commit=False)
            new_review.bookname=bookname
            new_review.save()
            return redirect('crazy_book_club_app:bookname',bookname_id=bookname_id)
    #display blank or invalid form
    context={'bookname':bookname, 'form':form}
    return render(request,'crazy_book_club_app/new_review.html',context)

@login_required
def edit_review(request, review_id):
    '''edit existing review'''
    review=Review.objects.get(id=review_id)
    bookname=review.bookname
    if bookname.owner!=request.user:
        raise Http404
    if request.method!='POST':
        #initial request must fill out form
        form=ReviewForm(instance=review)
    else:
        #post data submitted
        form=ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('crazy_book_club_app:bookname', bookname_id=bookname.id)
    context= {'review':review, 'bookname':bookname,'form':form}
    return render(request,'crazy_book_club_app/edit_review.html',context)