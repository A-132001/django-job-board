# Generated by Django 4.0.6 on 2022-07-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='JobsImages/'),
            preserve_default=False,
        ),
    ]
