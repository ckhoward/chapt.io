from django.contrib import admin
from . import models
from .models import Book, Author, Chapter


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


#may have to remove this class
class RatingInline(admin.TabularInline):
    model = models.Rating


class ChapterAdmin(admin.ModelAdmin):
    inlines = [
        RatingInline,
    ]


class RatingAdmin(admin.ModelAdmin):
    pass



admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(models.Rating)