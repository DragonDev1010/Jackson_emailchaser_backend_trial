# Generated by Django 4.2 on 2023-04-20 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connectedMail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectedmail',
            name='user',
        ),
    ]
