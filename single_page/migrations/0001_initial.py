# Generated by Django 4.0.1 on 2022-01-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hp', models.CharField(max_length=100)),
                ('maxhp', models.CharField(max_length=100)),
                ('gold', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housename', models.CharField(max_length=100)),
                ('housepoints', models.CharField(max_length=100)),
            ],
        ),
    ]
