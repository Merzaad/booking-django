# Generated by Django 3.2.9 on 2021-12-10 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='destination',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
