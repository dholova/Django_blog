# Generated by Django 4.1.6 on 2023-02-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Зображення'),
            preserve_default=False,
        ),
    ]
