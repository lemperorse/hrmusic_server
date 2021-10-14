# Generated by Django 3.2.4 on 2021-06-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0007_rename_plan_plan_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heartsong',
            name='heartrate',
        ),
        migrations.AddField(
            model_name='heartsong',
            name='heartrate_end',
            field=models.FloatField(default=100, max_length=120),
        ),
        migrations.AddField(
            model_name='heartsong',
            name='heartrate_start',
            field=models.FloatField(default=60, max_length=120),
        ),
    ]