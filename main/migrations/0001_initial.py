# Generated by Django 2.2.3 on 2019-09-09 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
