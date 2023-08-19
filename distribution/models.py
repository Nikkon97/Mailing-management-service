from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='почта', unique=True)
    comment = models.CharField(**NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Distribution(models.Model):
    emailing_time = models.DateTimeField
    periodicity = models.IntegerField
    mailing_status = models.BooleanField

    def __str__(self):
        return f'{self.emailing_time}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Message(models.Model):
    title = models.CharField(max_length=250, verbose_name='Тема')
    body = models.CharField(default=None, verbose_name='Сообщение')

    def __str__(self):
        return f'Тема сообщения: {self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Logs(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата и время последней рассылки')
    status = models.BooleanField()
    response = models.CharField(max_length=250, verbose_name='Ответ сервера')

    def __str__(self):
        return f'{self.status} ({self.datetime})'

    class Meta:
        verbose_name = 'логи'
        verbose_name_plural = 'логи'
