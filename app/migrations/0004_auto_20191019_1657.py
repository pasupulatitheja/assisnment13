# Generated by Django 2.2.3 on 2019-10-19 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191019_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]