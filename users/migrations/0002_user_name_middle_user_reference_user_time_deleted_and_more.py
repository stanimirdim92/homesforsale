# Generated by Django 4.2.1 on 2023-05-22 16:28

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="name_middle",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="middle name"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="reference",
            field=models.CharField(
                default="c", max_length=128, unique=True, verbose_name="reference"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="time_deleted",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="deleted at"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="time_modified",
            field=models.DateTimeField(auto_now=True, verbose_name="modified at"),
        ),
        migrations.AddField(
            model_name="user",
            name="title",
            field=models.CharField(blank=True, max_length=10, verbose_name="title"),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                db_index=True,
                error_messages={"unique": "A user with that email already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.core.validators.EmailValidator()],
                verbose_name="email",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="time_created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="created at"),
        ),
        migrations.AlterField(
            model_name="user",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, unique=True, verbose_name="uuid"
            ),
        ),
    ]
