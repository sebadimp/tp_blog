from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

CATEGORIA_OPCIONES = (
    ('vacio','-----------------'),
    ('cuidados','Cuidados'),
    ('alimentación', 'Alimentación'),
    ('entretenimiento','Entretenimiento'),
    ('lugares_y_paseos','Lugares y Paseos'),
    ('enfermedades','Enfermedades'),
    ('curiosidades','Curiosidades'),
)
class Post(models.Model):
    idautor= models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    autor=models.CharField('Autor',max_length=50,null=False,blank=False)
    titulo=models.CharField('Título',max_length=100,null= False, blank=False,unique=True)
    categoria=models.CharField('Categoría',max_length=30,null= False, blank=False, choices=CATEGORIA_OPCIONES,default='vacio')
    descripcion=models.CharField('Descripción',max_length=150,null= False, blank=False)
    contenido=RichTextField(null= False, blank=False)
    imagen = models.ImageField(upload_to='images/', null= True, blank=True, )
    fecha_creacion=models.DateField('Fecha de Creacion', auto_now = True)

    def __str__(self):
        return f'{self.titulo} |'
    

    

    