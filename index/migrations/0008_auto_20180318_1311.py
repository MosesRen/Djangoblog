# Generated by Django 2.0.3 on 2018-03-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20180318_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
