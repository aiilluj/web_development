# Лабораторная работа №2: Модели Django. ORM
**Вариант 3 (Комментарии)**

**Цель:** Изучить создание моделей в Django, выполнение миграций, работу с ORM через консоль Django, продемонстрировать CRUD-операции.

---

## 1. Создание модели (`models.py`)
Модель описывает структуру таблицы в базе данных. Откройте `news/models.py`.

```python
from django.db import models

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.user_name}: {self.text[:30]}'
Описание полей:

user_name — имя пользователя (строка до 100 символов).

email — электронная почта (с валидацией формата).

text — текст комментария (неограниченной длины).

created_at — дата создания (устанавливается автоматически).

is_moderated — прошел ли комментарий модерацию (по умолчанию False).

rating — оценка (целое число, по умолчанию 5).

2. Миграции
После создания или изменения модели нужно обновить структуру базы данных.

В терминале (с активированным (venv)) выполните:

bash
python manage.py makemigrations
python manage.py migrate
В папке news/migrations/ появится файл 0001_initial.py, а в базе данных (db.sqlite3) — таблица news_comment.

3. Работа с ORM (через консоль Django)
Запустите интерактивную консоль:

bash
python manage.py shell
Внутри консоли импортируйте модель:

python
from news.models import Comment
CREATE (Создание записей)
python
# Способ 1: Через конструктор
c1 = Comment(user_name='Анна', email='anna@mail.ru', text='Отличная статья!', rating=5)
c1.save()

# Способ 2: Через менеджер объектов (автоматически сохраняет)
Comment.objects.create(user_name='Иван', email='ivan@mail.ru', text='Полезно', rating=4, is_moderated=True)
READ (Чтение записей)
python
# Получить все записи
Comment.objects.all()

# Фильтрация (например, прошедшие модерацию)
Comment.objects.filter(is_moderated=True)

# Исключение
Comment.objects.exclude(rating=5)

# Получение одной записи по ID (pk)
Comment.objects.get(pk=1)
UPDATE (Обновление)
python
c = Comment.objects.get(pk=1)
c.is_moderated = True
c.save() # Сохраняем изменения
DELETE (Удаление)
python
c = Comment.objects.get(pk=1)
c.delete()
Для выхода из консоли введите:

python
exit()
4. Главное задание варианта
Вывести все комментарии, прошедшие модерацию.

В консоли shell выполните:

python
moderated = Comment.objects.filter(is_moderated=True)
for c in moderated:
    print(f'{c.user_name} ({c.email}) — {c.rating}/5: {c.text}')
5. Ответы на контрольные вопросы
Что такое модель в Django?
Класс Python, описывающий структуру таблицы БД. Наследуется от models.Model.

Типы полей?
CharField, TextField, IntegerField, DateTimeField, BooleanField, EmailField, ImageField.

blank=True и null=True?
blank — поле может быть пустым в формах. null — в БД может храниться NULL.

Что такое миграции?
Механизм применения изменений моделей к базе данных. Команды: makemigrations (создать), migrate (применить).

Что такое ORM?
Object-Relational Mapping — работа с БД через Python-объекты без прямого написания SQL.

Разница filter() и get()?
filter() возвращает QuerySet (список). get() возвращает один объект (ошибка, если записей 0 или >1).

Для чего нужен __str__?
Для читаемого строкового представления объекта (в админке, консоли, шаблонах).

Что будет, если сделать makemigrations, но не migrate?
Файл миграции создастся, но таблица в базе данных не появится.

6. Частые ошибки
Ошибка	Решение
no such table: news_comment	Не выполнена команда python manage.py migrate
ModuleNotFoundError	Проверить, что модель импортирована: from news.models import Comment
DoesNotExist	Записи с таким pk нет (проверьте ID)
IndentationError	Нарушены отступы в models.py (используйте 4 пробела)
Итог
Создана модель Comment.

Выполнены миграции (создана таблица в БД).

Освоены CRUD-операции через ORM в консоли Django.

Выведены все промодерированные комментарии (выполнено задание варианта).