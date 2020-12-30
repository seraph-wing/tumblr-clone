# Generated by Django 3.1.2 on 2020-12-30 14:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20201230_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, default='self', related_name='is_followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
