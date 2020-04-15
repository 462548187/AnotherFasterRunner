# Generated by Django 2.1.3 on 2020-04-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('fastrunner', '0015_config_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.BooleanField(blank=True, choices=[(0, '失败'), (1, '成功')], default=0, verbose_name='报告状态'),
            preserve_default=False,
        ),
    ]