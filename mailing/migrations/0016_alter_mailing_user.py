# Generated by Django 4.2.3 on 2023-07-22 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailing', '0015_alter_mailing_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='user',
            field=models.ForeignKey(default=users.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
