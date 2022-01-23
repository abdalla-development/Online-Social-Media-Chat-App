# Generated by Django 3.2.7 on 2021-09-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=5000)),
                ('last_name', models.CharField(max_length=5000)),
                ('email', models.CharField(max_length=5000)),
                ('password', models.CharField(max_length=5000)),
                ('birth_day', models.CharField(max_length=5000)),
                ('gender', models.CharField(max_length=5000)),
                ('phone_number', models.CharField(max_length=5000)),
                ('address', models.CharField(max_length=5000)),
                ('city', models.CharField(max_length=5000)),
                ('country', models.CharField(max_length=5000)),
                ('postal_code', models.CharField(max_length=5000)),
                ('about_me', models.CharField(max_length=5000)),
                ('bio', models.CharField(max_length=5000)),
                ('friends', models.IntegerField()),
                ('age', models.IntegerField()),
                ('profile_picture', models.CharField(max_length=500)),
            ],
        ),
    ]