# Generated by Django 2.2.4 on 2019-08-20 02:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('siteparser', '0004_auto_20190819_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlparsetimeshift',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 2, 14, 26, 598086, tzinfo=utc), verbose_name='Start time'),
        ),
    ]
