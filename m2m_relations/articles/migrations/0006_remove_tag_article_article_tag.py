# Generated by Django 4.2.1 on 2023-05-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_tag_tag_name_remove_article_tag_tag_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.tag'),
        ),
    ]
