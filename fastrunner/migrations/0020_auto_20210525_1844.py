# Generated by Django 2.2 on 2021-05-25 18:44

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fastrunner', '0019_auto_20210411_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='ci_metadata',
            field=jsonfield.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='project',
            name='yapi_base_url',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='yapi的openapi url'),
        ),
        migrations.AlterField(
            model_name='project',
            name='yapi_openapi_token',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='yapi openapi的token'),
        ),
    ]
