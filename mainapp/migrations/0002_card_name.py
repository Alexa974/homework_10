# pylint: disable=W,C,R
# Generated by Django 4.2 on 2023-04-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="name",
            field=models.CharField(
                blank=True, default="Карточка ", max_length=32, unique=True
            ),
        ),
    ]
