from django.urls import path
from .views import *
from blogs.views import blogs

urlpatterns = [
    path('',blogs,name="welcome"),
    path('collections/',my_collections,name="views-collection"),
    path('collections/<str:slug>/delete/',remove_collection,name="delete-collection"),
    path('articles/news/',authenticated,name="preminium"),
]
