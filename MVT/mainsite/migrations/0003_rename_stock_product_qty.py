# Generated by Django 3.2 on 2022-11-01 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20221030_0253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='qty',
        ),
    ]
