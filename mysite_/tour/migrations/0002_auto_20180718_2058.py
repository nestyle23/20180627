# Generated by Django 2.0.6 on 2018-07-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='city',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tour',
            name='nation',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tour',
            name='who',
            field=models.TextField(max_length=200),
        ),
    ]