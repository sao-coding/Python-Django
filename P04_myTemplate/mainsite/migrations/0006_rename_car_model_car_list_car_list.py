# Generated by Django 4.1.3 on 2022-11-06 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainsite", "0005_remove_tv_list_tvno"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car_list",
            old_name="car_model",
            new_name="car_list",
        ),
    ]