from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'created_at')