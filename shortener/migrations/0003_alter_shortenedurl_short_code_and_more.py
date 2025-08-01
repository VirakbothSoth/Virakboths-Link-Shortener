# Generated by Django 5.1.4 on 2025-04-07 09:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_shortenedurl_short_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_code',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
