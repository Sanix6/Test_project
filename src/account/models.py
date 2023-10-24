from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    phone = models.CharField("Телефон", max_length=255, unique=True)
    code = models.CharField("Код активации", max_length=6, null=True, blank=True)
    number_auth = models.CharField('Авторизация по телефону', max_length=255)
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField(max_length=100)
    birthday = models.IntegerField('День рождение')
    floor_type = [
        ('male', 'Мужской пол'),
        ('female', 'Женский пол'),
        ('no', 'Не указано')
    ]
    floor = models.CharField('Пол', max_length=25, choices=floor_type, default='no')
    language_type = [
        ('male', 'Кыргыз тили'),
        ('female', 'Русский язык'),
    ]
    language = models.CharField('Язык', max_length=100, choices=language_type)
    family_status_type = [
        ('male', 'Холост(не женат)'),
        ('female', 'Холостая(не замужем)'),
    ]
    family_status = models.CharField('Семейное положение', max_length=100, choices=family_status_type)
    social_status = models.CharField('Социальное положение', max_length=100)
    place_of_living = models.CharField('Место проживание', max_length=100)
    children_have = models.CharField('Имеет ли детей', max_length=100)
    pets = models.BooleanField('Имеет ли домашних животных', default=True)


    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return f'{self.phone},{self.code}'
