# Generated by Django 3.2.5 on 2021-07-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20210714_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, help_text='Contact Image', upload_to='static/media'),
        ),
    ]
