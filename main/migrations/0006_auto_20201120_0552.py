# Generated by Django 3.1.1 on 2020-11-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201120_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtaskcomment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='comment',
            field=models.TextField(),
        ),
    ]
