# Generated by Django 4.1.4 on 2022-12-27 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="blog/images/"),
        ),
    ]
