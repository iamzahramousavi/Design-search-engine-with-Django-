# Generated by Django 4.1.4 on 2023-01-20 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("context", "0004_idf_tfidflist_delete_tf_rename_context_contexts_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Contexts",
            new_name="DataScraped",
        ),
    ]
