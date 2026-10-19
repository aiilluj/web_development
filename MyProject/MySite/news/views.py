from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment


def index(request):
    # Получаем все комментарии
    comments = Comment.objects.all()

    # Формируем контекст — данные для передачи в шаблон
    context = {
        'comments': comments,
        'title': 'Список комментариев'
    }

    # Рендерим шаблон и передаем туда контекст
    return render(request, 'news/index.html', context)

def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')
# Create your views here.
