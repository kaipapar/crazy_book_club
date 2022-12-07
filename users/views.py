from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    '''register new cbc user'''
    if request.method != 'POST':
        #display empty form
        form=UserCreationForm()
    else:
        #process input form data
        form= UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            #log the user in and hten redirect to home page
            login(request, new_user)
            return redirect('crazy_book_club_app:index')
    #display an empty or invalid form
    context={'form':form}
    return render(request, 'users/register.html',context) #use users/register.html or users/register.html


