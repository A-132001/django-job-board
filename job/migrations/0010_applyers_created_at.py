# Generated by Django 4.0.6 on 2022-07-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_applyers'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyers',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
