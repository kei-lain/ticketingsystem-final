# Generated by Django 3.2.8 on 2021-10-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20211011_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'EndUser'), (2, 'Employee'), (3, 'Admin')], null=True),
        ),
    ]