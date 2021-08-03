# Generated by Django 3.2.5 on 2021-07-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, help_text='Contact Image', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, help_text='Phone Number'),
        ),
    ]
