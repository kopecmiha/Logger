# Generated by Django 3.1.7 on 2022-05-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0006_auto_20220504_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='user_agent',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]