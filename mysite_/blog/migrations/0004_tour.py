# Generated by Django 2.0.6 on 2018-07-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nation', models.TextField(max_length=200)),
                ('city', models.TextField(max_length=200)),
                ('who', models.TextField(max_length=200)),
                ('to_date', models.DateTimeField()),
                ('from_date', models.DateTimeField()),
                ('comment', models.TextField()),
                ('image', models.ImageField(upload_to='%Y/%m/%d/orig')),
                ('filtered_image', models.ImageField(upload_to='%Y/%m/%d/filtered')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
