# Generated by Django 3.2.13 on 2023-11-15 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20231115_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarioanswer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='comentarioforum',
            name='image',
        ),
    ]
