# Generated by Django 3.2.6 on 2022-04-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Child', '0004_auto_20220410_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
