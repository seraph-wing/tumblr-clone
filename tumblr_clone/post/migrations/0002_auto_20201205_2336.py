# Generated by Django 3.1.2 on 2020-12-05 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='notes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.note'),
        ),
    ]
