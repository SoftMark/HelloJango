# Generated by Django 3.1.4 on 2021-01-11 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chihuahua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('gender', models.CharField(choices=[('suka', 'сука'), ('kobel', 'кобель')], default='suka', max_length=20, verbose_name='Пол')),
                ('rewards', models.TextField(verbose_name='Награды')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('age', models.CharField(choices=[('puppy', 'щенок'), ('adult', 'взрослый')], default='adult', max_length=20, verbose_name='Щенок/Взрослый')),
                ('sale', models.CharField(choices=[('yes', 'да'), ('not', 'нет')], default='yes', max_length=20, verbose_name='Для продажи')),
                ('teeth', models.CharField(max_length=7, verbose_name='Зубы')),
                ('weight', models.FloatField(verbose_name='Вес')),
                ('color', models.TextField(verbose_name='Окрас')),
                ('type_of_wool', models.CharField(max_length=25, verbose_name='Тип шерсти')),
                ('father', models.CharField(max_length=50, verbose_name='Папа')),
                ('mother', models.CharField(max_length=50, verbose_name='Мама')),
                ('pedigree', models.CharField(max_length=50, verbose_name='Родословная')),
                ('pedigree_link', models.TextField(verbose_name='Ссылка на родословную')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Чихуахуа',
                'verbose_name_plural': 'Чишки',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('chihuahua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='settings_content.chihuahua')),
            ],
        ),
    ]
