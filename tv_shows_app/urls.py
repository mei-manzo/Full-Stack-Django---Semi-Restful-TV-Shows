from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new', views.add),
    path('shows', views.all),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>', views.show), 
    path('shows/<int:id>/destroy', views.delete),
    path('shows/create', views.create),
    path('shows/<int:id>/update', views.update),
]