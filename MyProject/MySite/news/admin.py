from django.contrib import admin
from .models import Comment, Author, Book

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Какие колонки показывать в общем списке
    list_display = ('id', 'user_name', 'email', 'rating', 'is_moderated', 'created_at')
    # По каким колонкам можно кликать для редактирования
    list_display_links = ('id', 'user_name')
    # По каким полям работает поиск (появится строка поиска)
    search_fields = ('user_name', 'email', 'text')
    # Фильтры справа
    list_filter = ('is_moderated', 'rating')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'isbn')
    list_display_links = ('id', 'title')
    list_editable = ('year',)  # <--- ВОТ ЭТО ДОБАВЛЕНО
    search_fields = ('title', 'isbn')
    list_filter = ('author', 'year')