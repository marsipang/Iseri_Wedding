# Generated by Django 3.0.2 on 2020-02-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0015_auto_20200205_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingparty',
            name='FirstName',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='weddingparty',
            name='LastName',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='weddingparty',
            name='Title',
            field=models.TextField(max_length=50),
        ),
    ]
