# Generated by Django 2.2.1 on 2019-07-07 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190707_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='time_start',
            field=models.DateTimeField(),
        ),
    ]
