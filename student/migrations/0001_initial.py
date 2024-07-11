# Generated by Django 5.0.7 on 2024-07-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('grade', models.CharField(max_length=11, verbose_name='Класс')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Студент',
            },
        ),
    ]
