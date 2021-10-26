# Generated by Django 3.2.8 on 2021-10-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_person_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='troubleshooting',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='equipmentTag',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]