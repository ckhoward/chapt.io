# Generated by Django 2.0.6 on 2018-06-20 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20180619_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating_choice',
            field=models.IntegerField(choices=[('Boring', 'Boring'), ('Engaging', 'Engaging')], default=0),
        ),
    ]
