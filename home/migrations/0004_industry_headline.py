# Generated by Django 3.2 on 2023-08-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='headline',
            field=models.TextField(blank=True, null=True),
        ),
    ]
