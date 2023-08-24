from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс - команда для создания суперпользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='djangotest1997@yandex.ru',
            first_name='django',
            last_name='python',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password('123')

        user.save()
