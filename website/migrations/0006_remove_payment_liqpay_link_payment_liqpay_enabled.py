# Generated by Django 4.0.3 on 2022-05-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_legal_privacy_policy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='liqpay_link',
        ),
        migrations.AddField(
            model_name='payment',
            name='liqpay_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
