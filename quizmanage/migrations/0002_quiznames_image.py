# Generated by Django 4.2.7 on 2023-11-08 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizmanage", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiznames",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="quiznimage"),
        ),
    ]
