# Generated by Django 3.0.8 on 2021-03-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210304_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='bio',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]
