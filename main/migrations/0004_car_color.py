# Generated by Django 2.2.3 on 2019-09-11 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190910_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='Blue', max_length=20),
            preserve_default=False,
        ),
    ]