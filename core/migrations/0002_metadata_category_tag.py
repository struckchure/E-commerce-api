# Generated by Django 4.1.3 on 2022-11-08 13:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MetaData",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.TextField()),
                (
                    "type",
                    models.CharField(
                        choices=[("TAG", "Tag"), ("CATEGORY", "Category")],
                        max_length=100,
                    ),
                ),
            ],
            options={
                "verbose_name": "Meta data",
                "verbose_name_plural": "Meta datas",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("core.metadata",),
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("core.metadata",),
        ),
    ]
