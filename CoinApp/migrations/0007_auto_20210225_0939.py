# Generated by Django 3.1.7 on 2021-02-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoinApp', '0006_auto_20210225_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='finCoins',
            field=models.IntegerField(default=0),
        ),
    ]
