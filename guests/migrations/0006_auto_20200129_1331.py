# Generated by Django 3.0.2 on 2020-01-29 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0005_guest_invitationid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='AddressLine1',
            new_name='Address',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='AddressLine2',
        ),
    ]