# Generated by Django 5.1.2 on 2024-10-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='data',
            field=models.TextField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=350),
        ),
    ]