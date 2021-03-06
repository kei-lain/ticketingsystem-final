# Generated by Django 3.2.8 on 2021-10-10 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20211010_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'User'), (2, 'Employee'), (3, 'Admin')], null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='userEffected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.role'),
        ),
    ]
