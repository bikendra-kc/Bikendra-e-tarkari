# Generated by Django 3.0.5 on 2020-05-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='ProfilePicture',
            field=models.ImageField(upload_to='pp'),
        ),
    ]