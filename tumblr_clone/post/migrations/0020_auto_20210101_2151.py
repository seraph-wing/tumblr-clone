# Generated by Django 3.1.2 on 2021-01-01 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_auto_20210101_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reblog',
            old_name='reblogger',
            new_name='reblogged_from',
        ),
    ]
