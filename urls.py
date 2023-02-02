from django.contrib import admin
from django.urls import path
from . import views
app_name = 'context'
urlpatterns = [
    path("content/", views.first),
    path("tokens/", views.token),
    path("", views.home),
    path("idf/", views.createIdf),
    path("tfidf/", views.createTfIdf),
    path("nav/", views.navigate),
    # path("tfcrf/", views.createTfCRF),
    # path("category/", views.createCategory),
]
