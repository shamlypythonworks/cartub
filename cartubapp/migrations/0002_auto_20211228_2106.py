# Generated by Django 3.2.5 on 2021-12-29 02:06

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartubapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default=builtins.print, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
