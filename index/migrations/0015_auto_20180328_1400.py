# Generated by Django 2.0.3 on 2018-03-28 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20180327_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtext',
            name='catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.ArticleCatagory', verbose_name='分类'),
        ),
    ]
