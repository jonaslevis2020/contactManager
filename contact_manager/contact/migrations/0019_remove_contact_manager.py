# Generated by Django 3.2.5 on 2021-07-21 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0018_alter_contact_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='manager',
        ),
    ]