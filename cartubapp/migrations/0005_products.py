# Generated by Django 3.2.5 on 2021-12-29 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartubapp', '0004_auto_20211229_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='albums')),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField(default=False)),
                ('categ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartubapp.category')),
            ],
        ),
    ]