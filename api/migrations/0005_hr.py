# Generated by Django 4.1.7 on 2023-02-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='HR',
            fields=[
                ('사번', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('구분', models.CharField(default='', max_length=5)),
                ('이름', models.CharField(default='', max_length=5)),
                ('영문이름', models.CharField(default='', max_length=20)),
                ('근무지', models.CharField(default='', max_length=5)),
                ('부서', models.CharField(default='', max_length=5)),
                ('팀', models.CharField(default='', max_length=20)),
                ('직위', models.CharField(default='', max_length=5)),
                ('직책', models.CharField(default='', max_length=5)),
                ('입사일', models.DateField()),
                ('근속일', models.IntegerField(default='')),
                ('주민등록번호', models.CharField(default='', max_length=20)),
                ('생년월일', models.DateField()),
                ('연락처', models.CharField(default='', max_length=20)),
                ('비상연락망', models.CharField(default='', max_length=20)),
                ('회사이메일', models.CharField(default='', max_length=50)),
                ('개인이메일', models.CharField(default='', max_length=50)),
                ('주소', models.CharField(default='', max_length=70)),
                ('최종학력', models.CharField(default='', max_length=10)),
                ('최종학위', models.CharField(default='', max_length=10)),
                ('학교', models.CharField(default='', max_length=20)),
                ('전공', models.CharField(default='', max_length=20)),
                ('학점', models.CharField(default='', max_length=10)),
                ('입사구분', models.CharField(default='', max_length=10)),
                ('경력사항1', models.CharField(default='', max_length=20)),
                ('경력사항2', models.CharField(default='', max_length=20)),
                ('경력사항3', models.CharField(default='', max_length=20)),
                ('경력사항4', models.CharField(default='', max_length=20)),
                ('경력사항5', models.CharField(default='', max_length=20)),
                ('자격사항1', models.CharField(default='', max_length=20)),
                ('자격사항2', models.CharField(default='', max_length=20)),
                ('자격사항3', models.CharField(default='', max_length=20)),
                ('자격사항4', models.CharField(default='', max_length=20)),
                ('자격사항5', models.CharField(default='', max_length=20)),
                ('어학사항1', models.CharField(default='', max_length=20)),
                ('어학사항2', models.CharField(default='', max_length=20)),
                ('어학사항3', models.CharField(default='', max_length=20)),
                ('어학사항4', models.CharField(default='', max_length=20)),
                ('어학사항5', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
