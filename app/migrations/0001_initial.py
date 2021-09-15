# Generated by Django 3.2.7 on 2021-09-15 16:11

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=150)),
                ('about_you', models.TextField(max_length=400)),
                ('education', models.CharField(max_length=250)),
                ('career', models.CharField(max_length=150)),
                ('job_1_start', models.DateField()),
                ('job_1_end', models.DateTimeField()),
                ('job_1_details', models.CharField(max_length=250)),
                ('job_2_start', models.DateTimeField()),
                ('job_2_end', models.DateTimeField()),
                ('job_2_details', models.CharField(max_length=250)),
                ('job_3_start', models.DateTimeField()),
                ('job_3_end', models.DateTimeField()),
                ('job_3_details', models.CharField(max_length=250)),
                ('references', models.CharField(max_length=250)),
                ('image', models.ImageField(default='post/default.png', upload_to=app.models.user_directory_path)),
            ],
        ),
    ]
