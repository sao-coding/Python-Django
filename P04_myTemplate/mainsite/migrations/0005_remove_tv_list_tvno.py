# Generated by Django 4.1.3 on 2022-11-05 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainsite", "0004_remove_engtv_list_tvno"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tv_list",
            name="tvno",
        ),
    ]