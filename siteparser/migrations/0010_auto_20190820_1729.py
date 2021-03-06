# Generated by Django 2.2.4 on 2019-08-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteparser', '0009_auto_20190820_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlparsetimeshift',
            name='status_success',
            field=models.BooleanField(default=False, verbose_name='Success'),
        ),
        migrations.AlterField(
            model_name='urlparsetimeshift',
            name='start_time',
            field=models.DateTimeField(default=None, verbose_name='Start time UTC'),
        ),
    ]
