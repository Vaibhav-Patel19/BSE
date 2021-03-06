# Generated by Django 3.2.4 on 2021-07-09 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_barmenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishName', models.CharField(blank=True, max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('cooked', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Ordered Food',
            },
        ),
    ]
