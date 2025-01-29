# Generated by Django 3.2.13 on 2023-11-13 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('base', '0022_palavraproibida'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PalavraProibida',
        ),
        migrations.AddField(
            model_name='comentario',
            name='content_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
