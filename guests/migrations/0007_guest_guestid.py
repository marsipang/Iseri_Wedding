# Generated by Django 3.0.2 on 2020-01-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0006_auto_20200129_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='GuestID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
