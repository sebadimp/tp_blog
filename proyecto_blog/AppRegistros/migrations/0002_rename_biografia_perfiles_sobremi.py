# Generated by Django 4.1.3 on 2022-12-05 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppRegistros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfiles',
            old_name='biografia',
            new_name='sobremi',
        ),
    ]
