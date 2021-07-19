# Generated by Django 3.2.4 on 2021-06-17 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20210617_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='duration',
        ),
        migrations.AddField(
            model_name='duration',
            name='program',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='exercise.program'),
            preserve_default=False,
        ),
    ]
