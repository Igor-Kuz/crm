# Generated by Django 3.1.2 on 2020-11-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201119_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dead_line',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(),
        ),
    ]
