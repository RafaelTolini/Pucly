# Generated by Django 3.2.13 on 2023-11-12 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_notification_notification_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created']},
        ),
    ]
