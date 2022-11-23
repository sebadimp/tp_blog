from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import datetime


CATEGORIA_OPCIONES = (
    ('vacio','------------------'),
    ('cuidados','Cuidados'),
    ('alimentación', 'Alimentación'),
    ('entretenimiento','Entretenimiento'),
)
class Post(models.Model):
    titulo=models.CharField('Titulo',max_length=100,null= False, blank=False)
    subtitulo=models.CharField('Subtitulo',max_length=100,null= False, blank=False)
    categoria=models.CharField('Categoria',max_length=30,null= False, choices=CATEGORIA_OPCIONES,default='vacio')
    #contenido=models.TextField('Contenido',max_length=255)
    contenido=RichTextField(blank=True,null=True)
    fecha=models.DateField('Fecha de Creacion', default=datetime.datetime.now)
    autor=models.CharField('Autor',max_length=100,null= False, blank=False)
