# Generated by Django 3.1.1 on 2020-11-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201120_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='avatars/img_avatar2.png', upload_to='avatars/'),
        ),
    ]
