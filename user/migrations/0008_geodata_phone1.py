# Generated by Django 3.0.5 on 2020-05-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200510_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='geodata',
            name='phone1',
            field=models.CharField(max_length=13, null=True),
        ),
    ]