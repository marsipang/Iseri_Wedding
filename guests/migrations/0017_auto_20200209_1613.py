# Generated by Django 3.0.2 on 2020-02-10 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0016_auto_20200205_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='id',
        ),
        migrations.AlterField(
            model_name='guest',
            name='GuestID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='InvitationID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guests.Email'),
        ),
    ]