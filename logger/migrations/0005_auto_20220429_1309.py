# Generated by Django 3.1.7 on 2022-04-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0004_logger_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='user_uuid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
