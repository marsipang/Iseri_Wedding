# Generated by Django 3.0.2 on 2020-02-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0009_auto_20200130_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeddingParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.TextField()),
                ('LastName', models.TextField()),
                ('Relation', models.TextField()),
                ('Title', models.TextField()),
            ],
        ),
    ]