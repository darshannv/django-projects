# Generated by Django 4.0.1 on 2024-01-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='instamojo_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
