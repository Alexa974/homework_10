# Generated by Django 4.2 on 2023-04-30 19:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0010_alter_card_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="card",
            old_name="name",
            new_name="title",
        ),
    ]