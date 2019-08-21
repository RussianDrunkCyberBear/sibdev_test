# Generated by Django 2.2.4 on 2019-08-20 07:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siteparser', '0006_auto_20190820_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlparsetimeshift',
            name='response_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='urlparsetimeshift',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start time'),
        ),
    ]
