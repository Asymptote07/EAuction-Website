# Generated by Django 5.0.1 on 2024-02-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_bid_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='time',
            field=models.CharField(default='10 February, 2024', max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(default='10 February, 2024', max_length=20),
        ),
        migrations.AlterField(
            model_name='listings',
            name='time',
            field=models.CharField(default='10 February, 2024', max_length=20),
        ),
    ]
