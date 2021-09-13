# Generated by Django 3.2.4 on 2021-07-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='barMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drinktype', models.CharField(blank=True, choices=[('1', 'Beer'), ('2', 'Cocktail'), ('3', 'Gin'), ('4', 'Red Wine'), ('5', 'Sparkling Wine'), ('6', 'Vodka'), ('7', 'Whiskey'), ('8', 'White Wine')], max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('total_qty', models.IntegerField(null=True)),
                ('savings', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('low', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('high', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('className', models.CharField(blank=True, max_length=50)),
                ('recommended_drink', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Bar Menu',
            },
        ),
    ]