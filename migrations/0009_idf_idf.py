# Generated by Django 4.1.4 on 2023-01-22 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("context", "0008_rename_docid_datascraped_id_rename_idfid_idf_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="idf",
            name="idf",
            field=models.FloatField(default=1),
        ),
    ]