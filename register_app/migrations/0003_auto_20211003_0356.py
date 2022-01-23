# Generated by Django 3.2.7 on 2021-10-03 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register_app', '0002_auto_20210930_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='bio',
        ),
        migrations.AlterField(
            model_name='register',
            name='profile_picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='register',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
