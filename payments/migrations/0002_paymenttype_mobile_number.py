# Generated by Django 3.2.4 on 2022-03-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttype',
            name='mobile_Number',
            field=models.IntegerField(default=None, max_length=10),
        ),
    ]
