# Generated by Django 3.2.7 on 2021-09-27 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qGen', '0002_alter_paragraph_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='EndUser',
        ),
    ]
