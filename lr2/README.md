МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ
Федеральное государственное автономное образовательное учреждение высшего образования
«СЕВЕРО-КАВКАЗСКИЙ ФЕДЕРАЛЬНЫЙ УНИВЕРСИТЕТ»
Институт перспективной инженерии
Департамент цифровых робототехнических систем и электроники
Межинститутская базовая кафедра

# Отчет к лабораторной работе № 2

**Тема:** Модели. CRUD.
**Дисциплина:** Разработка web-приложений

## Выполнила:

Студент группы ПИЖ-б-о-25-1 (1),
направление подготовки: 09.03.04 «Программная инженерия»
Алейникова Юлия Андреевна

## Проверила:

ассистент межинститутской базовой кафедры департамента цифровых, робототехнических систем и электроники института перспективной инженерии

Белик Ангелина Игоревна

Ставрополь 2026

---

**Цель работы:** разработка моделей, научиться проводить миграцию данных, работа с базой данных.

## Ход выполнения лабораторной работы

**Вариант 3. Комментарии**

- Модель: `Comment` (поля: `user_name`, `email`, `text`, `created_at`, `is_moderated`).
- Добавить поле `rating` (целое число от 1 до 5).
- Вывести все комментарии, прошедшие модерацию.

### 1. Создание модели Comment

В файле `news/models.py` создана модель `Comment`.

```python
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.user_name}: {self.text[:30]}'
```

![Задание](screen/1.PNG)


*(Рисунок 1 – модель Comment)*

| Поле | Тип | Назначение |
| :--- | :--- | :--- |
| `user_name` | `CharField(100)` | Имя пользователя |
| `email` | `EmailField` | Email с валидацией |
| `text` | `TextField` | Текст комментария |
| `created_at` | `DateTimeField(auto_now_add=True)` | Дата создания |
| `is_moderated` | `BooleanField(default=False)` | Прошёл модерацию |
| `rating` | `IntegerField(default=5)` | Оценка от 1 до 5 |

*(Таблица 1 – Описание полей)*

Метод `__str__` возвращает имя пользователя и первые 30 символов текста.

### 2. Миграции

Создана миграция:

```bash
python manage.py makemigrations
```

![Задание](screen/2.PNG)


*(Рисунок 2 – python manage.py makemigrations)*

Применена миграция:

```bash
python manage.py migrate
```

![Задание](screen/3.PNG)


*(Рисунок 3 – Результат применения миграции)*

В базе данных появилась таблица `news_comment`:

![Задание](screen/4.PNG)


*(Рисунок 4 – Таблица news_comment)*

### 3. Настройка медиафайлов

В `settings.py` добавлено:

```python
import os

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

![Задание](screen/5.PNG)


*(Рисунок 5 – Файл settings.py)*

В корневом `urls.py` добавлен маршрут:

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

![Задание](screen/6.PNG)


*(Рисунок 6 – Файл MySite\urls.py)*

### 4. Работа с ORM (консоль Django)

Запуск консоли:

```bash
python manage.py shell
```

Импорт модели:

```python
from news.models import Comment
```

![Задание](screen/7.PNG)


*(Рисунок 7 – Работа с ORM)*

### 5. Создание записей

Создано 7 записей:

```python
c1 = Comment(user_name='Анна', email='anna@mail.ru', text='Отличная статья!', rating=5)
c1.save()

c2 = Comment.objects.create(
    user_name='Иван',
    email='ivan@mail.ru',
    text='Полезная информация, спасибо.',
    rating=4,
    is_moderated=True
)

# ... и другие записи
```

![Задание](screen/8.PNG)


*(Рисунок 8 – Создание записей)*

### 6. Чтение данных

Все записи:

```python
Comment.objects.all()
```

Прошедшие модерацию:

```python
Comment.objects.filter(is_moderated=True)
```

Комментарии с рейтингом выше 3:

```python
Comment.objects.filter(rating__gt=3)
```

Одна запись по id:

```python
Comment.objects.get(pk=1)
```

Исключение:

```python
Comment.objects.exclude(is_moderated=False)
```

![Задание](screen/9.PNG)


*(Рисунок 9 – Чтение данных)*

### 7. Обновление

Изменить одну запись:

```python
c = Comment.objects.get(pk=6)
c.is_moderated = True  # одобрить комментарий Сергея
c.save()
```

Проверить:

```python
Comment.objects.filter(is_moderated=True)
```

![Задание](screen/10.PNG)


*(Рисунок 10 – Добавление комментария в список)*

Массовое обновление:

```python
Comment.objects.filter(rating=5).update(is_moderated=True)
```

### 8. Удаление

Удалить одну запись с `pk=7`:

```python
c = Comment.objects.get(pk=7)
c.delete()
```

Массовое удаление:

```python
Comment.objects.filter(rating__lt=3).delete()
```

Удалит все комментарии с рейтингом меньше 3.

Проверка:

```python
Comment.objects.all()
```

![Задание](screen/11.PNG)


*(Рисунок 11 – Удаление)*

### 9. Результаты работы

Вывод всех комментариев, прошедших модерацию:

```python
moderated = Comment.objects.filter(is_moderated=True)
for c in moderated:
    print(f'{c.user_name} ({c.email}) — {c.rating}/5: {c.text}')
```

![Задание](screen/12.PNG)


*(Рисунок 12 – Результаты)*

![Задание](screen/13.PNG)


**Ссылка на гитхаб:** https://github.com/aiilluj/web_development.git

## Контрольные вопросы

**1. Что такое модель в Django и для чего она используется?**
Модель – это класс Python, наследник `django.db.models.Model`, описывающий структуру таблицы БД. Используется для хранения и извлечения данных через ORM без написания SQL.

**2. Какие типы полей вы знаете?**
`CharField`, `TextField`, `IntegerField`, `DateTimeField`, `BooleanField`, `EmailField`, `ImageField`, `ForeignKey` и др.

**3. Чем отличаются `blank=True` и `null=True`?**
`blank=True` – поле может быть пустым в формах. `null=True` – в БД может храниться `NULL`.

**4. Что такое миграции и зачем они нужны?**
Миграции – способ применения изменений моделей к схеме БД. Команды:
- `python manage.py makemigrations` – создать миграции.
- `python manage.py migrate` – применить.
- `python manage.py sqlmigrate <app> <name>` – показать SQL.

**5. Как создать суперпользователя?**
```bash
python manage.py createsuperuser
```

**6. Что такое ORM? Основные методы CRUD?**
ORM – Object-Relational Mapping, работа с БД через Python-объекты.
- Create: `Model.objects.create(...)`, `obj.save()`
- Read: `all()`, `filter()`, `get()`, `exclude()`
- Update: `obj.save()`, `QuerySet.update()`
- Delete: `obj.delete()`

**7. В чём разница между `filter()` и `get()`?**
`filter()` возвращает `QuerySet` (может быть пустым или содержать много записей). `get()` возвращает один объект, выбрасывает исключение при отсутствии или множестве записей.

**8. Как настроить загрузку изображений?**
В `settings.py`: `MEDIA_ROOT`, `MEDIA_URL`. В `urls.py`: `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` при `DEBUG=True`.

**9. Для чего нужен `__str__`?**
Для читаемого строкового представления объекта (в админке, консоли, шаблонах).

**10. Что произойдёт, если выполнить `makemigrations`, но не `migrate`?**
Файл миграции будет создан, но изменения не применятся к БД. Таблица не появится.

## Вывод

Разработали модели, научились проводить миграцию данных, работали с базой данных.