# Generated by Django 5.1.1 on 2024-09-26 11:43

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_alter_profile_bio_alter_profile_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name="artwork",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
