# Generated by Django 4.0.1 on 2024-01-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruits',
            name='price',
            field=models.IntegerField(),
        ),
    ]
