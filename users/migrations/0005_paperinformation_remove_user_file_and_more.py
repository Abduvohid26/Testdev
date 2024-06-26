# Generated by Django 5.0.6 on 2024-06-12 05:02

import django.core.validators
import users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_country_delete_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('key_words', models.CharField(max_length=5, validators=[django.core.validators.MaxValueValidator(5)])),
                ('section', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='users/sections/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.doc', '.docx']), users.utils.validate_file_size])),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='file',
        ),
        migrations.RemoveField(
            model_name='user',
            name='key_words',
        ),
        migrations.RemoveField(
            model_name='user',
            name='section',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
    ]
