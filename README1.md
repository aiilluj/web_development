# Лабораторная работа №1: Создание виртуального окружения. Контроллеры и маршруты

**Цель:** Настроить виртуальное пространство, разработать контроллер приложения и организовать маршруты.

---

## 1. Создание виртуального окружения

Виртуальное окружение (venv) нужно для изоляции зависимостей проекта.

1. Создайте папку проекта (например, `MyProject`).
2. Откройте терминал в PyCharm (или командную строку) и перейдите в эту папку.
3. Выполните команду:

   ```bash
   python -m venv venv
   ```

Активируйте окружение (для Windows):

```powershell
venv\Scripts\activate
```

В начале строки терминала появится `(venv)`.

## 2. Установка Django

Устанавливаем фреймворк в активированное окружение:

```bash
pip install Django
```

Проверить установку можно командой `pip list` или `python -m django --version`.

## 3. Создание проекта и приложения

Создайте Django-проект:

```bash
django-admin startproject MySite
cd MySite
```

Создайте приложение `news`:

```bash
python manage.py startapp news
```

## 4. Регистрация приложения

Откройте файл `MySite/settings.py` и добавьте приложение `news` в список `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',  # <-- Добавить эту строку
]
```

## 5. Создание контроллеров (views.py)

Контроллеры принимают HTTP-запрос и возвращают HTTP-ответ.

Откройте файл `news/views.py` и напишите:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world')

def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
```

## 6. Настройка маршрутов (urls.py)

Маршрутизатор связывает URL-адреса с функциями-контроллерами.

### 6.1. Корневой маршрутизатор

Откройте `MySite/urls.py` (внутри одноименной папки проекта) и настройте его так:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')), # Подключаем маршруты приложения news
]
```

### 6.2. Маршруты приложения

Создайте новый файл `news/urls.py` и добавьте в него:

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),         # http://127.0.0.1:8000/news/
    path('test/', test),     # http://127.0.0.1:8000/news/test/
]
```

## 7. Запуск сервера

В терминале (с активированным `(venv)` и находясь в папке с `manage.py`) выполните:

```bash
python manage.py runserver
```

Проверьте в браузере:

- http://127.0.0.1:8000/news/ → выведет `Hello world`
- http://127.0.0.1:8000/news/test/ → выведет `Тестовая страница`
- http://127.0.0.1:8000/admin/ → страница входа в админку

## 8. Частые ошибки

| Ошибка | Причина | Решение |
|--------|---------|---------|
| `python: command not found` | Python не в PATH | Переустановить Python с галочкой "Add to PATH" |
| `django-admin: command not found` | Не активирован venv | `venv\Scripts\activate` |
| `ModuleNotFoundError` | Приложение не зарегистрировано | Проверить `INSTALLED_APPS` в `settings.py` |
| `404 Page not found` | Неверный маршрут | Проверить `path()` в `urls.py` |
| `(venv)` пропал | Закрыли/перезапустили терминал | Активировать заново |

## Итог

- Создано и настроено виртуальное окружение.
- Установлен Django.
- Создан проект `MySite` и приложение `news`.
- Написаны контроллеры `index` и `test`.
- Настроена вложенная маршрутизация через `include`.
- Проверена работа сервера и вывод страниц в браузере.