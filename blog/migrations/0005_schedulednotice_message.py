# Generated by Django 2.2.1 on 2022-09-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220906_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulednotice',
            name='message',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]