# Generated by Django 4.0.2 on 2022-02-09 18:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddAuction',
            new_name='Auction',
        ),
    ]
