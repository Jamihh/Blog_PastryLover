# Generated by Django 5.1.1 on 2024-10-21 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_image_alter_article_datedepublicatiion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='dateDePublicatiion',
            new_name='dateDePublication',
        ),
    ]