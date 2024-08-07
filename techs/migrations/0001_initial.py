# Generated by Django 5.0.6 on 2024-08-07 05:08

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creators', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='slug')),
                ('logo', models.ImageField(blank=True, default='tech.png', upload_to='', verbose_name='Logo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('history', django_ckeditor_5.fields.CKEditor5Field(verbose_name='History')),
                ('visibility', models.BooleanField(default=False)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='description')),
                ('documentation', models.URLField(max_length=50, verbose_name='Documentation')),
                ('creator', models.ManyToManyField(to='creators.creator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tech',
                'verbose_name_plural': 'Techs',
                'ordering': ['name'],
            },
        ),
    ]
