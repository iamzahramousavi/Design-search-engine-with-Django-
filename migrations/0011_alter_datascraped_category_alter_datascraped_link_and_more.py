# Generated by Django 4.1.4 on 2023-01-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("context", "0010_datascraped_bodyorg_datascraped_titleorg_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datascraped",
            name="category",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="datascraped",
            name="link",
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="datascraped",
            name="pubDate",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="datascraped",
            name="tags",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="datascraped",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="datascraped",
            name="titleOrg",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]