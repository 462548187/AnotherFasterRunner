# Generated by Django 2.2 on 2020-10-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastrunner', '0013_visit_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='url',
            field=models.CharField(db_index=True, max_length=255, verbose_name='请求地址'),
        ),
        migrations.AlterField(
            model_name='casestep',
            name='url',
            field=models.CharField(max_length=255, verbose_name='请求地址'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='url',
            field=models.CharField(max_length=255, verbose_name='被访问的url'),
        ),
    ]