# Generated by Django 4.2.2 on 2023-07-01 09:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_alter_listings_watchlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listings",
            name="watchlist",
        ),
    ]
