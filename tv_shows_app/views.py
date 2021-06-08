from django.shortcuts import render, HttpResponse, redirect
from .models import *

def add(request):
    return render(request, "add_show.html")

def edit(request):
    return render(request, "edit_show.html")

def show(request, id): #has id in url, add id param
    context = {
        "this_show": Shows.objects.get(id=1)
    }
    return render(request, "tv_show.html", context)

def all(request):
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request, "all_shows.html", context)


def create(request):
    if request.method=='POST':
        Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release-date'], description=request.POST['description'])
        return redirect('/shows/'+id)
    context = {
        "this_show": Shows.objects.get(id=request.POST['id'])
    }
    return redirect('/shows/'+id, context)