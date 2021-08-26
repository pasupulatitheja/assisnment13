# Generated by Django 2.2.3 on 2019-10-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.IntegerField(default=False, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]