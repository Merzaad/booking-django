# Generated by Django 3.2.9 on 2021-12-10 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='size',
            field=models.IntegerField(),
        ),
    ]