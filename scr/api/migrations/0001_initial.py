# Generated by Django 3.2.8 on 2021-11-05 18:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField(verbose_name='Новость')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]