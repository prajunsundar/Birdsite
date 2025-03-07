# Generated by Django 4.2.16 on 2024-11-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='birds',
            name='slug',
            field=models.SlugField(default='exit', max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='birds',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='birds',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
