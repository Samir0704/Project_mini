from django.contrib import admin
from django.urls import path, include
from test_app import views

urlpatterns = [
    path ('books/',views.BookListApiView.as_view(),name='book'),
    path('authors/',views.AuthorListApiView.as_view(),name='author')
]