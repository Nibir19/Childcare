# Generated by Django 3.2.6 on 2022-04-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Child', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
