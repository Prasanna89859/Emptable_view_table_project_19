# Generated by Django 4.2.6 on 2023-12-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_employeetable_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetable',
            name='Job',
            field=models.IntegerField(),
        ),
    ]
