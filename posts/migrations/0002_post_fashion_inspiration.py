# Generated by Django 3.2.21 on 2023-12-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fashion_inspiration',
            field=models.TextField(blank=True, null=True),
        ),
    ]
