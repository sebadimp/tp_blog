# Generated by Django 4.1.3 on 2022-12-05 01:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50, verbose_name='Autor')),
                ('titulo', models.CharField(max_length=100, unique=True, verbose_name='Título')),
                ('categoria', models.CharField(choices=[('vacio', '-----------------'), ('cuidados', 'Cuidados'), ('alimentación', 'Alimentación'), ('entretenimiento', 'Entretenimiento'), ('lugares_y_paseos', 'Lugares y Paseos')], default='vacio', max_length=30, verbose_name='Categoría')),
                ('descripcion', models.CharField(max_length=150, verbose_name='Descripción')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de Creacion')),
                ('idautor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
