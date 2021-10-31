# Generated by Django 3.2.8 on 2021-10-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoSmokingStages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя стадии')),
                ('time', models.FloatField(verbose_name='Время (д)')),
                ('time_descr', models.CharField(max_length=100, verbose_name='Описание времени')),
                ('text', models.TextField(verbose_name='Описание стадии')),
            ],
        ),
    ]
