# Лабораторная работа №3: Шаблоны. Админка Django
**Вариант 3 (Комментарии)**

---

## 1. Структура проекта

Для того чтобы Django мог находить HTML-файлы, нужно создать правильную структуру папок внутри приложения `news`:

```text
news/
 ├── migrations/
 ├── templates/
 │    └── news/
 │         └── index.html  <-- файл шаблона
 ├── admin.py
 ├── models.py
 └── views.py
```

## 2. Контроллер (views.py)

Вместо склеивания HTML-строк через `HttpResponse`, используем функцию `render`, которая передает данные (контекст) в шаблон.

```python
from django.shortcuts import render
from .models import Comment

def index(request):
    # Получаем все комментарии из БД
    comments = Comment.objects.all()
    
    # Формируем контекст — словарь с данными для шаблона
    context = {
        'comments': comments,
        'title': 'Список комментариев'
    }
    
    # Рендерим HTML-шаблон и передаем контекст
    return render(request, 'news/index.html', context)


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
```

## 3. Шаблон (news/templates/news/index.html)

Используются основные конструкции шаблонизатора Django:

- `{{ ... }}` — вывод переменных.
- `{% for ... %}` — циклы.
- `{% if ... %}` — условия.
- `|date:"..."` — фильтры для форматирования дат.

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>

    {% for item in comments %}
        <div style="border: 1px solid #ccc; margin-bottom: 15px; padding: 10px;">
            <p><strong>Пользователь:</strong> {{ item.user_name }}</p>
            <p><strong>Email:</strong> {{ item.email }}</p>
            <p><strong>Комментарий:</strong> {{ item.text }}</p>
            <p><strong>Оценка:</strong> {{ item.rating }} / 5</p>
            <p><strong>Дата:</strong> {{ item.created_at|date:"Y-m-d H:i" }}</p>
            
            <p>
                <strong>Статус:</strong> 
                {% if item.is_moderated %}
                    <span style="color: green;">Прошел модерацию</span>
                {% else %}
                    <span style="color: red;">На модерации</span>
                {% endif %}
            </p>
        </div>
    {% empty %}
        <p>Комментариев пока нет.</p>
    {% endfor %}
</body>
</html>
```

## 4. Модель (models.py)

Для удобной работы в админке и правильной сортировки добавляем `verbose_name` к полям и класс `Meta`.

```python
from django.db import models

class Comment(models.Model):
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_moderated = models.BooleanField(default=False, verbose_name='Прошел модерацию')
    rating = models.IntegerField(default=5, verbose_name='Оценка')

    def __str__(self):
        return f'{self.user_name}: {self.text[:30]}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']  # Новые сверху
```

⚠️ **Важно:** После изменения `models.py` обязательно выполните в терминале:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Админка (admin.py)

Регистрируем модель `Comment` с кастомным классом `ModelAdmin` для настройки колонок, поиска и фильтров.

```python
from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Колонки в общем списке
    list_display = ('id', 'user_name', 'email', 'rating', 'is_moderated', 'created_at')
    # Ссылки для перехода к редактированию
    list_display_links = ('id', 'user_name')
    # Поля для поиска
    search_fields = ('user_name', 'email', 'text')
    # Фильтры справа
    list_filter = ('is_moderated', 'rating')
```

## 6. Настройки (settings.py)

Для того чтобы даты в шаблоне и админке выводились на русском языке, измените параметр:

```python
LANGUAGE_CODE = 'ru'
```

## 7. Создание администратора

В терминале (с активированным `(venv)`) выполните:

```bash
python manage.py createsuperuser
```

Введите:

- **Имя пользователя:** `admin`
- **Email:** пропустить (Enter)
- **Пароль:** придумать (если ругается на простой пароль — введите `y`)

Запустите сервер:

```bash
python manage.py runserver
```

## 8. Проверка результата

**Главная страница (http://127.0.0.1:8000/news/):**

- Отображается заголовок «Список комментариев».
- Каждый комментарий в рамке.
- Выводятся: Имя, Email, Текст, Оценка, Дата (на русском).
- Статус модерации выделен цветом (зеленый / красный).

**Админка (http://127.0.0.1:8000/admin/):**

- Вход под логином `admin`.
- Слева раздел «NEWS» → «Комментарии».
- В списке колонки: ID, Имя, Email, Оценка, Модерация, Дата.
- Работает поиск по имени/email/тексту.
- Работают фильтры справа (по модерации и оценке).
- Можно добавлять, редактировать и удалять записи.

## 9. Частые ошибки

| Ошибка | Причина | Решение |
|--------|---------|---------|
| `NameError: name 'Comment' is not defined` | Не импортирована модель | `from .models import Comment` в `views.py` |
| `TemplateDoesNotExist` | Неверный путь к шаблону | Проверить папку `news/templates/news/` |
| `(venv)` пропал | Окружение не активно | `.\venv\Scripts\Activate.ps1` |
| `No such table: news_comment` | Миграции не применены | `python manage.py migrate` |
| Админка на английском | Не изменен `LANGUAGE_CODE` | `LANGUAGE_CODE = 'ru'` в `settings.py` |
| `Fatal error in launcher` при `pip` | Пробел в пути к проекту | Использовать `python -m pip install ...` |

## 10. Итог

В ходе лабораторной работы:

- Освоен механизм шаблонов Django.
- Изучены теги (`for`, `if`, `empty`) и фильтры (`date`).
- Настроен вывод данных из БД на HTML-страницу.
- Настроена административная панель (поиск, фильтры, колонки).
- Модель `Comment` полностью русифицирована.
- Настроена локализация (`LANGUAGE_CODE = 'ru'`).