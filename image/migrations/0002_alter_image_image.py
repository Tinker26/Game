# Generated by Django 4.0.2 on 2022-02-20 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.CharField(max_length=300),
        ),
    ]
