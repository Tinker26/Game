# Generated by Django 3.1.1 on 2022-02-11 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Categorya',
                'verbose_name_plural': 'Categoryalar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Komandalar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(default='')),
                ('data', models.DateField()),
                ('image', models.CharField(max_length=100)),
                ('achko', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='game.category')),
            ],
            options={
                'verbose_name': 'Komanda',
                'verbose_name_plural': 'Komandalar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='')),
                ('image', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categorya', to='game.category')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'Blog',
                'ordering': ['name'],
            },
        ),
    ]
