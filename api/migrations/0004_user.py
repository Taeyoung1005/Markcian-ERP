# Generated by Django 4.1.5 on 2023-02-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_coa_코드_alter_product_제품코드"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(default="", max_length=100, unique=True)),
                ("nickname", models.CharField(default="", max_length=100, unique=True)),
                ("name", models.CharField(default="", max_length=100)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
