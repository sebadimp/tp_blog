# Generated by Django 4.1.3 on 2022-11-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0006_alter_post_autor_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(max_length=100, null=True, verbose_name='Autor'),
        ),
    ]
