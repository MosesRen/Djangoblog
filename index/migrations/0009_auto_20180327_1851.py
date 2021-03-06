# Generated by Django 2.0.3 on 2018-03-27 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20180318_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='类别')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.RemoveField(
            model_name='blogtext',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='blogtext',
            name='type',
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='img',
            field=models.ImageField(upload_to='avatar/'),
        ),
        migrations.AddField(
            model_name='blogtext',
            name='catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.ArticleCatagory', verbose_name='分类'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogtext',
            name='tags',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.ArticleTag', verbose_name='标签'),
            preserve_default=False,
        ),
    ]
