# Generated by Django 3.2.4 on 2021-10-08 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_foodorder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barmenu',
            name='className',
        ),
        migrations.RemoveField(
            model_name='barmenu',
            name='old_price',
        ),
        migrations.RemoveField(
            model_name='barmenu',
            name='savings',
        ),
        migrations.RemoveField(
            model_name='barmenu',
            name='total_qty',
        ),
    ]