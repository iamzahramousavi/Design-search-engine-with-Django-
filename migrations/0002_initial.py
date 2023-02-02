# Generated by Django 4.1.4 on 2023-01-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("context", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="context",
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
                ("link", models.URLField(blank=True, max_length=600, null=True)),
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                ("pubDate", models.CharField(blank=True, max_length=200, null=True)),
                ("body", models.CharField(blank=True, max_length=10000, null=True)),
                ("category", models.CharField(blank=True, max_length=200, null=True)),
                ("tags", models.CharField(blank=True, max_length=200, null=True)),
                ("createAt", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tokens",
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("posting", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]