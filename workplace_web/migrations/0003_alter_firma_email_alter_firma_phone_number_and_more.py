# Generated by Django 4.2.5 on 2023-09-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workplace_web', '0002_alter_pracovnipozice_popis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='firma',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='firma',
            name='popis',
            field=models.TextField(blank=True, null=True),
        ),
    ]