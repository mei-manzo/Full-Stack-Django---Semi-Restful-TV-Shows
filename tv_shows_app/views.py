from django.shortcuts import render, HttpResponse, redirect
from .models import *

def add(request):
    return render(request, "add_show.html")

def edit(request):
    return render(request, "edit_show.html")

def edit_this(request): #similar to def create, we are performing an action then redirecting
    if request.method == 'POST':
        return redirect(f"/shows/{new_show.id}/edit")
    elif request.method == 'GET':
        return redirect('/shows/3')
    return redirect('/shows/new')

def show(request, id): #has id in url, add id param
    context = {
        "this_show": Shows.objects.get(id=id)
    }
    return render(request, "tv_show.html", context)

def all(request): #used for our "all" display page
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request, "all_shows.html", context)


def create(request):
    if request.method=='POST':
        new_show = Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release-date'], description=request.POST['description'])
        print(new_show.id)
        return redirect(f"/shows/{new_show.id}") #just needed to convert this to a f string to get it to read
        #redirects to def show
    return redirect('/shows/new')