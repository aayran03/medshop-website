# Generated by Django 5.0.6 on 2024-06-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0006_orders"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="phone",
            field=models.CharField(default="", max_length=25),
        ),
    ]
