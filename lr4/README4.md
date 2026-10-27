# Лабораторная работа №4: Связи моделей (Библиотека)
**Вариант 3**

## 1. models.py

```python
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # ... (bio, photo)
    def __str__(self): return f'{self.last_name} {self.first_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    isbn = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
```

> **Важно:** Класс `Author` должен быть объявлен выше класса `Book`.

## 2. Миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

## 3. admin.py

```python
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'isbn')
    list_editable = ('year',) 
    list_filter = ('author', 'year')
    search_fields = ('title', 'isbn')
```

## 4. Проверка

- Создать 3 авторов.
- Создать 6 книг (выбрать автора из списка).
- Удалить автора → книги удаляются (CASCADE).
- В SQLiteStudio: таблица `news_book`, поле `author_id` — внешний ключ.

## 5. Частые ошибки

| Ошибка | Решение |
|--------|---------|
| `NameError: Author is not defined` | Класс `Author` должен быть выше `Book` в `models.py` |
| `no such table` | Забыли сделать `migrate` |
| `Pillow is not installed` | `python -m pip install Pillow` |
| `list_editable` не работает | Поле не должно быть в `list_display_links` |

## 6. Итог

- Созданы две связанные модели (`Author`, `Book`).
- Настроен `ForeignKey` с `on_delete=CASCADE` и `related_name`.
- Выполнены миграции.
- Настроена админка (фильтры, поиск, редактирование).
- Проверено каскадное удаление.