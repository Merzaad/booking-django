# Generated by Django 3.2.9 on 2021-12-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20211210_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(),
        ),
    ]