# Generated by Django 3.2.8 on 2021-11-06 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apptime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.TextField(verbose_name='Название игры')),
                ('price_old', models.CharField(max_length=10, verbose_name='Старая цена')),
                ('price_new', models.CharField(max_length=10, verbose_name='Новая цена')),
                ('sale_percent', models.CharField(max_length=10, verbose_name='Скидка')),
                ('cover', models.TextField(verbose_name='Cover')),
                ('app_link', models.TextField(verbose_name='AppStore')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
