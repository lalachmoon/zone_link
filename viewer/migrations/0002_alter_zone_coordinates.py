# Generated by Django 5.1.4 on 2025-02-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='coordinates',
            field=models.JSONField(),
        ),
    ]
