# Generated by Django 4.2.6 on 2024-01-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oscar_invoices", "0004_date_banking_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="document",
            field=models.FileField(
                blank=True, null=True, upload_to="invoices", verbose_name="Document"
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="legalentity",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="legalentityaddress",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
