# Generated by Django 4.2.4 on 2023-11-04 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workplace_web', '0016_firma_popis_firma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firma',
            name='popis_firma',
        ),
    ]