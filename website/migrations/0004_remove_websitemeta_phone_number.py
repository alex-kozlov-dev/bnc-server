# Generated by Django 4.0.3 on 2022-05-24 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitemeta',
            name='phone_number',
        ),
    ]
