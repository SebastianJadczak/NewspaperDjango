# Generated by Django 3.0.2 on 2020-01-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200114_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default=''),
        ),
    ]