# Generated by Django 4.0.1 on 2022-01-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_page', '0002_remove_boss_hp_remove_boss_maxhp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='hp',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='boss',
            name='maxhp',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='houses',
            name='housepoints',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
