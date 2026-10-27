# Лабораторная работа №5: Внедрение Bootstrap в шаблоны
**Вариант 3 (Комментарии)**

## 1. Подключение Bootstrap

В файл `news/templates/news/index.html` в секцию `<head>` добавлен CSS, а перед `</body>` — JS:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css">
...
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
```

## 2. Navbar (Навигация)

Добавлена панель навигации с ссылками на главную и админку:

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary shadow-sm">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">MySite</a>
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav me-auto">
        <li class="nav-item"><a class="nav-link" href="/">Главная</a></li>
        <li class="nav-item"><a class="nav-link" href="/admin/">Админка</a></li>
      </ul>
    </div>
  </div>
</nav>
```

## 3. Карточки (Cards) и тег cycle

Каждый комментарий обернут в карточку. Для чередования цвета оценок (красный/зеленый) использован тег `{% cycle %}`. Для статусов — бейджи.

```html
{% for item in comments %}
<div class="col-md-12 mb-3">
    <div class="card shadow-sm">
        <div class="card-header bg-white">
            {{ item.user_name }} ({{ item.email }})
        </div>
        <div class="card-body">
            <h5 class="card-title {% cycle 'text-danger' 'text-success' %}">
                Оценка: {{ item.rating }} / 5
            </h5>
            <p class="card-text">{{ item.text }}</p>
        </div>
        <div class="card-footer text-muted bg-white d-flex justify-content-between">
            <small>{{ item.created_at|date:"Y-m-d H:i:s" }}</small>
            {% if item.is_moderated %}
                <span class="badge bg-success">Модерация пройдена</span>
            {% else %}
                <span class="badge bg-danger">На модерации</span>
            {% endif %}
        </div>
    </div>
</div>
{% endfor %}
```

## 4. Проверка

- Страница обновилась, появился серый фон (`bg-light`).
- Сверху работает меню навигации.
- Комментарии выводятся в карточках с тенями.
- Оценки чередуются по цвету (красный/зеленый).
- Бейджи статуса модерации корректно отображаются.

## 5. Частые ошибки

| Ошибка | Решение |
|--------|---------|
| Стили не применились | Проверить ссылку на CDN (интернет) |
| `TemplateSyntaxError` | Тег `{% empty %}` должен быть внутри `{% for %}` |
| Меню не сворачивается на телефоне | Не подключен JS Bootstrap перед `</body>` |

## 6. Итог

- Подключен Bootstrap через CDN.
- Создана адаптивная панель навигации.
- Вывод данных оформлен через карточки (Card).
- Использован тег `{% cycle %}` для динамических стилей.
- Использованы бейджи для статусов.
