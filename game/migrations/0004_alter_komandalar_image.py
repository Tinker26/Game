# Generated by Django 4.0.2 on 2022-02-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20220212_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komandalar',
            name='image',
            field=models.CharField(max_length=300),
        ),
    ]
