# Generated by Django 4.2.3 on 2023-07-06 03:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0010_rename_bids_bid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="image_url",
        ),
    ]
