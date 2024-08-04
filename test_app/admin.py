from django.contrib import admin
from test_app.models import Book,Category,Author
# Register your models here.
admin.site.register(Book)
# admin.site.register(Category)
admin.site.register(Author)


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}