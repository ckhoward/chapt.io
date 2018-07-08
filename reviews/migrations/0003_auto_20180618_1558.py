# Generated by Django 2.0.6 on 2018-06-18 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Author'),
        ),
    ]