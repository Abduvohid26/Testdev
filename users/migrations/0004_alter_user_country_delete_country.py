# Generated by Django 5.0.6 on 2024-06-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(default=1, max_length=500, verbose_name='Country'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
