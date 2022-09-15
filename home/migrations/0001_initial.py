# Generated by Django 4.1.1 on 2022-09-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('date', models.DateTimeField()),
                ('msg', models.TextField(blank=True)),
            ],
        ),
    ]
