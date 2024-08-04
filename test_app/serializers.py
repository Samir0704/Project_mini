from rest_framework import serializers
from test_app.models import Book,Category,Author

class AuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields ='__all__'
        # exclude =()


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
        # exclude = ()
        

class BookModelSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer(many=True,read_only=True)
    category = CategoryModelSerializer( many=True,read_only=True)


    class Meta:
        model = Book
        # fields = '__all__'
        # extra_fields = ['author','category']
        fields = ['id','title','author','category']
