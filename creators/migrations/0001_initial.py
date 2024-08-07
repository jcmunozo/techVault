# Generated by Django 5.0.6 on 2024-08-07 05:08

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Creator name')),
                ('slug', models.SlugField(max_length=35, unique=True, verbose_name='slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('biography', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Biography')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Creator',
                'verbose_name_plural': 'Creators',
            },
        ),
    ]
