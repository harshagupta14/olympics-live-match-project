# Generated by Django 2.2.1 on 2022-09-06 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_notified'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='schedule',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='scheduleTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ScheduledNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]