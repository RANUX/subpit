# Generated by Django 3.2.7 on 2021-10-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0002_alter_subscriber_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='phone',
            field=models.CharField(blank=True, max_length=30, verbose_name='phone'),
        ),
    ]
