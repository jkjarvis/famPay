# Generated by Django 3.2.7 on 2021-09-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]