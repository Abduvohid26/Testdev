# Generated by Django 5.0.6 on 2024-06-12 05:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_paperinformation_remove_user_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperinformation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
