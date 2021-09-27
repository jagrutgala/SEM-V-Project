# Generated by Django 3.2.7 on 2021-09-27 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qGen', '0005_auto_20210927_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paragraph',
            name='username',
        ),
        migrations.CreateModel(
            name='ParaHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para_no', models.IntegerField()),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qGen.paragraph')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qGen.enduser')),
            ],
        ),
    ]
