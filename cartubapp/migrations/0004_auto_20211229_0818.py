# Generated by Django 3.2.5 on 2021-12-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartubapp', '0003_auto_20211229_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catname', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('img', models.ImageField(upload_to='photos')),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]
