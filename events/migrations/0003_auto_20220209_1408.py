# Generated by Django 3.2.10 on 2022-02-09 11:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20220209_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='datetime_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='datetime_start',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]