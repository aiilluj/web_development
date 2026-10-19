from django.db import models

class News(models.Model):

    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


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
        ordering = ['-created_at']


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    bio = models.TextField(blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='authors/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name']


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    year = models.IntegerField(verbose_name='Год издания')
    isbn = models.CharField(max_length=20, verbose_name='ISBN')

    # Связь с автором (ForeignKey)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,  # При удалении автора удаляются его книги
        related_name='books',  # Обратный доступ: author.books.all()
        verbose_name='Автор'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-year']