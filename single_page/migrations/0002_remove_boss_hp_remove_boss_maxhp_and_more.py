# Generated by Django 4.0.1 on 2022-01-11 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boss',
            name='hp',
        ),
        migrations.RemoveField(
            model_name='boss',
            name='maxhp',
        ),
        migrations.RemoveField(
            model_name='houses',
            name='housepoints',
        ),
    ]