# Generated by Django 5.0.6 on 2024-06-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=13)),
                ("email", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("timeStamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
