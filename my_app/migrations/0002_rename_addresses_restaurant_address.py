# Generated by Django 4.2.6 on 2023-10-14 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="restaurant",
            old_name="addresses",
            new_name="address",
        ),
    ]