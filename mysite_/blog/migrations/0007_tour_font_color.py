# Generated by Django 2.0.6 on 2018-07-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tour_background_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='font_color',
            field=models.TextField(default='black'),
        ),
    ]
