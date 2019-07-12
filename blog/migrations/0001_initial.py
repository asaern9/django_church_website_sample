# Generated by Django 2.2.1 on 2019-07-07 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('picture', models.ImageField(upload_to='Event/')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField()),
                ('reporter', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('picture', models.ImageField(upload_to='News/')),
            ],
        ),
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_sermon', models.DateTimeField()),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('format_video', models.FileField(upload_to='Sermon/Video/')),
                ('format_audio', models.FileField(upload_to='Sermon/Audio/')),
                ('format_doc', models.FileField(upload_to='Sermon/Document/')),
                ('title', models.CharField(max_length=100)),
                ('preacher', models.CharField(max_length=150)),
                ('content', models.TextField()),
            ],
        ),
    ]