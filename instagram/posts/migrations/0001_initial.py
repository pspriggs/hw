# Generated by Django 2.2 on 2019-04-23 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.CharField(blank=True, default='', max_length=500)),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('img', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
    ]
