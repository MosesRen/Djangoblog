# Generated by Django 2.0.3 on 2018-03-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20180327_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtext',
            name='tags',
            field=models.ManyToManyField(null=True, to='index.ArticleTag', verbose_name='标签'),
        ),
    ]
