# Generated by Django 3.0.8 on 2020-08-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200803_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='people',
            name='lname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
