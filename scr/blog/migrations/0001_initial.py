# Generated by Django 3.2.8 on 2021-10-31 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.TextField(verbose_name='Icon base64')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('intro', models.CharField(max_length=300, verbose_name='Интро')),
                ('text', models.TextField(verbose_name='Пост')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
            ],
        ),
    ]
