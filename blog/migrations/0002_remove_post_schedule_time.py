# Generated by Django 2.2.1 on 2022-09-02 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='schedule_time',
        ),
    ]
