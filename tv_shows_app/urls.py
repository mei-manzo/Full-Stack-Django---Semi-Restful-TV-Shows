from django.urls import path     
from . import views
urlpatterns = [
    path('shows/new', views.add),
    path('shows', views.all),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>', views.show), 
    path('shows/create', views.create),
    path('shows/edit_this', views.edit_this),
]