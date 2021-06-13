from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    return redirect('/shows')

def add(request):
    return render(request, "add_show.html")

def edit(request, id):
    context = {
        "updated_show": Shows.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)

def update(request, id):
    errors = Shows.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit")
    else:
        # if request.method=='POST':
        updated_show = Shows.objects.get(id=id)
        updated_show.title=request.POST['title']
        updated_show.network=request.POST['network']
        updated_show.release_date=request.POST['release-date']
        updated_show.description=request.POST['description']
        updated_show.save()
        messages.success(request, "TV Show successfully updated")
        return redirect(f"/shows/{id}")
    # return redirect('/shows') 

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
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
    # if request.method=='POST':
        new_show = Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release-date'], description=request.POST['description'])
        return redirect(f"/shows/{new_show.id}") #just needed to convert this to a f string to get it to read
    # return redirect('/shows/new')

def delete(request, id):
    delete_show = Shows.objects.get(id=id)
    delete_show.delete()
    return redirect('/shows')