# pylint: disable=W,C,R
# Generated by Django 4.2 on 2023-04-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0008_alter_card_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="name",
            field=models.CharField(max_length=32, null=True),
        ),
    ]
