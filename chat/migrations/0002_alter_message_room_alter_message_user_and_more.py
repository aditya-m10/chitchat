# Generated by Django 4.0.6 on 2022-07-13 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=1000000),
        ),
    ]
