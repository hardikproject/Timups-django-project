# Generated by Django 4.1.7 on 2023-02-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='buyer', max_length=100),
        ),
    ]