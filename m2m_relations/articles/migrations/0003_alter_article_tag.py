# Generated by Django 4.2.1 on 2023-05-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.tag'),
        ),
    ]
