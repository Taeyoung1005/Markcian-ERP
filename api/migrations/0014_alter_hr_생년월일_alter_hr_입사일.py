# Generated by Django 4.1.7 on 2023-02-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_hr_사번'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='생년월일',
            field=models.DateField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='입사일',
            field=models.DateField(default='', null=True),
        ),
    ]
