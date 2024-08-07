# Generated by Django 5.0.6 on 2024-08-07 05:08

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('techs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Feature name')),
                ('level', models.CharField(choices=[('BASIC', 'Basic'), ('INTERMEDIATE', 'Intermediate'), ('ADVANCED', 'Advanced')], default='BASIC', max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Description')),
                ('tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techs.tech')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
    ]
