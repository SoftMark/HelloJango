# Generated by Django 3.1.3 on 2021-01-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_content', '0002_auto_20210119_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chihuahua',
            name='reserve',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=20, verbose_name='В резерве'),
        ),
        migrations.AlterField(
            model_name='chihuahua',
            name='sale',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Да', max_length=20, verbose_name='Для продажи'),
        ),
    ]