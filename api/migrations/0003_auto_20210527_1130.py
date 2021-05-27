# Generated by Django 3.2.3 on 2021-05-27 08:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_follow_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.RemoveField(
            model_name='follow',
            name='author',
        ),
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
