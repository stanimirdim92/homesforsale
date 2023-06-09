# Generated by Django 4.2.1 on 2023-05-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_user_last_login_alter_user_name_first_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="company_vat_number",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="vat number"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="entity_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("CLIENT", "Client"),
                    ("AGENCY", "Agency"),
                    ("ORGANIZATION", "Organization"),
                ],
                default="CLIENT",
                max_length=128,
                null=True,
                verbose_name="type",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="reference_external",
            field=models.CharField(
                blank=True, max_length=128, null=True, verbose_name="reference external"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="title",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Mr", "Mr"),
                    ("Mrs", "Mrs"),
                    ("Miss", "Miss"),
                    ("Ms", "Ms"),
                    ("Dr", "Dr"),
                    ("Prof", "Prof"),
                    ("Sir", "Sir"),
                ],
                default="Mr",
                max_length=10,
                null=True,
                verbose_name="title",
            ),
        ),
    ]
