# Generated by Django 2.2.5 on 2021-05-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(max_length=50)),
                ('map_url', models.TextField(max_length=100)),
                ('user_id', models.IntegerField()),
                ('like', models.IntegerField(default=0)),
                ('create_time', models.DateField(auto_now=True)),
            ],
        ),
    ]
