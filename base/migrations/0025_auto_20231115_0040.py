# Generated by Django 3.2.13 on 2023-11-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_auto_20231113_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarioanswer',
            name='image',
            field=models.ImageField(default='profile.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='comentarioforum',
            name='image',
            field=models.ImageField(default='profile.png', null=True, upload_to=''),
        ),
    ]
