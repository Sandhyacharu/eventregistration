# Generated by Django 3.1.1 on 2021-02-21 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapplication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participantlist',
            old_name='institution',
            new_name='Age',
        ),
    ]
