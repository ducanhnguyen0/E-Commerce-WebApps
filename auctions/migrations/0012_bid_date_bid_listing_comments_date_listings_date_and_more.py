# Generated by Django 4.2.3 on 2023-07-07 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0011_remove_category_image_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="bid",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="bid",
            name="listing",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bid_listing",
                to="auctions.listings",
            ),
        ),
        migrations.AddField(
            model_name="comments",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="listings",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="listings",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="listings",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="listings",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=11),
        ),
    ]
