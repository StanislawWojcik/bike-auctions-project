# Generated by Django 4.0.2 on 2022-02-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_rename_addauction_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='type',
            field=models.CharField(choices=[('TOU', 'Touring'), ('MTB', 'MTB'), ('ROA', 'Road'), ('URB', 'Urban'), ('BMX', 'BMX'), ('ELE', 'Electric'), ('OTH', 'Other')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]
