from django.db import models


class GuestBook(models.Model):

    STATUS_CHOICE = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано')
    ]

    author = models.CharField(max_length=120, blank=False, null=False, verbose_name='Имя автора')
    email = models.EmailField(blank=False, null=False, verbose_name='Почта автора')
    text = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, null=False, blank=False, default=STATUS_CHOICE[0], verbose_name='Статус')
