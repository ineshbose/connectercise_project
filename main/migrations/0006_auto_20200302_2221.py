# Generated by Django 3.0.3 on 2020-03-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200302_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportingrequest',
            name='sessionID',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
