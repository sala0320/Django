# Generated by Django 3.0.2 on 2020-01-11 09:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20200111_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
