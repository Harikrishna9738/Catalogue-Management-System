# Generated by Django 3.0.1 on 2019-12-23 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CatalogueApp', '0002_auto_20191223_0731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specifications',
            old_name='vale',
            new_name='value',
        ),
    ]
