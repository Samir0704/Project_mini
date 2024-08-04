from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from test_app.models import  Book,Author
from rest_framework import status, viewsets
from rest_framework.response import Response
from test_app.serializers import BookModelSerializer
from rest_framework.generics import ListAPIView
from test_app.serializers import AuthorModelSerializer,BookModelSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Create your views here.

class BookListApiView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookModelSerializer
    # queryset = Book.objects.all()
    @method_decorator(cache_page(60*60))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_queryset(self):
        queryset = Book.objects.prefetch_related('author','category').all()
        return queryset

    # def get_queryset(self):
    #     queryset = Book.objects.select_related('author').all()
    #     return queryset
    
class AuthorListApiView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AuthorModelSerializer
    queryset= Author.objects.all()

    # def get_queryset(self):
    #     queryset = Author.objects.select_related('').all()
    #     return queryset



