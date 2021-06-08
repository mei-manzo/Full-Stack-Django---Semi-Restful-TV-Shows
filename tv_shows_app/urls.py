from django.urls import path     
from . import views
urlpatterns = [
    path('shows/new', views.add),
    path('shows', views.all),
    path('shows/2/edit', views.edit), #need to add param for '2'
    path('shows/<id>', views.show), #need to add param for '2'
    path('shows/create', views.create),
]