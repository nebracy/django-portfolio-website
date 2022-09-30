# Generated by Django 4.1.1 on 2022-09-30 12:56

from django.db import migrations


def load_initial_data(apps, schema_editor):
    pass


def delete_all_data(apps, schema_editor):
    Commit = apps.get_models('home', 'Commit')
    Commit.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data, delete_all_data)
    ]
