# Generated by Django 3.1.3 on 2021-03-03 15:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings_content', '0005_auto_20210209_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfigurations',
            name='Rich',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]