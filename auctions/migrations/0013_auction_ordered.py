# Generated by Django 4.0.2 on 2022-02-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_rename_item_order_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
