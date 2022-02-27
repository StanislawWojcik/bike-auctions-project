# Generated by Django 4.0.2 on 2022-02-24 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auction_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='picture',
        ),
        migrations.AddField(
            model_name='auction',
            name='image',
            field=models.ImageField(default=0, upload_to='images'),
            preserve_default=False,
        ),
    ]
