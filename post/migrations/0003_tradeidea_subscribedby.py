# Generated by Django 3.2.8 on 2021-11-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_tradeidea_createdby'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeidea',
            name='subscribedBy',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]