# pylint: disable=W,C,R,E
# Generated by Django 4.2 on 2023-04-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0005_alter_card_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="name",
            field=models.CharField(default="Карточка ", max_length=32, null=True),
        ),
    ]
