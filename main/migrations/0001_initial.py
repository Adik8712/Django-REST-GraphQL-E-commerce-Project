# Generated by Django 4.2.2 on 2023-06-20 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Image')),
                ('name', models.CharField(max_length=100, verbose_name='Category name')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]