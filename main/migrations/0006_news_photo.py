# Generated by Django 3.0.2 on 2020-01-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200114_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo'),
        ),
    ]