# Generated by Django 4.2.6 on 2023-10-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_children_have_profile_family_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.IntegerField(default=1, verbose_name='День рождение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='children_have',
            field=models.CharField(default=1, max_length=100, verbose_name='Имеет ли детей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='family_status',
            field=models.CharField(choices=[('male', 'Холост(не женат)'), ('female', 'Холостая(не замужем)')], default=1, max_length=100, verbose_name='Семейное положение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='floor',
            field=models.CharField(choices=[('male', 'Мужской пол'), ('female', 'Женский пол'), ('no', 'Не указано')], default='no', max_length=25, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('male', 'Кыргыз тили'), ('female', 'Русский язык')], default=1, max_length=100, verbose_name='Язык'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='number_auth',
            field=models.CharField(default=1, max_length=255, verbose_name='Авторизация по телефону'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='pets',
            field=models.BooleanField(default=True, verbose_name='Имеет ли домашних животных'),
        ),
        migrations.AddField(
            model_name='user',
            name='place_of_living',
            field=models.CharField(default=1, max_length=100, verbose_name='Место проживание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='social_status',
            field=models.CharField(default=1, max_length=100, verbose_name='Социальное положение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default=1, max_length=100, verbose_name='Фамилия'),
            preserve_default=False,
        ),
    ]
