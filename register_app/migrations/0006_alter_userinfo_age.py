# Generated by Django 3.2.7 on 2021-10-03 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0005_alter_userinfo_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
