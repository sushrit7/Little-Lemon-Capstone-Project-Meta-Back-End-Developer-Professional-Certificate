# Generated by Django 5.0.1 on 2024-01-03 21:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Menu",
            new_name="MenuItem",
        ),
    ]
