# Generated by Django 3.2.4 on 2021-11-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211008_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]