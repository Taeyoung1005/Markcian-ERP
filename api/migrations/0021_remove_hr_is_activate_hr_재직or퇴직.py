# Generated by Django 4.1.7 on 2023-03-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0020_hr_is_activate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hr",
            name="is_activate",
        ),
        migrations.AddField(
            model_name="hr",
            name="재직or퇴직",
            field=models.CharField(default="재직", max_length=2),
        ),
    ]
