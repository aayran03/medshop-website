# Generated by Django 5.0.6 on 2024-06-21 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=50)),
                ("desc", models.CharField(max_length=400)),
                ("pub_date", models.DateField()),
            ],
        ),
    ]
