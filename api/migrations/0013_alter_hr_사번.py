# Generated by Django 4.1.7 on 2023-02-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_hr_생년월일_alter_hr_입사일'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='사번',
            field=models.IntegerField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
