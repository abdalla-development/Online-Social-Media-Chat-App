# Generated by Django 3.2.7 on 2021-10-03 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0007_alter_userinfo_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]