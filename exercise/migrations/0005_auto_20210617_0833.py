# Generated by Django 3.2.4 on 2021-06-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0004_auto_20210617_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duration',
            name='program',
        ),
        migrations.AddField(
            model_name='program',
            name='duration',
            field=models.ManyToManyField(to='exercise.Duration'),
        ),
    ]
