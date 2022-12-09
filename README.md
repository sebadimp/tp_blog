# PROYECTO FINAL - TP BLOG

por Sebastian D'Imperio.

Este es un proyecto realizado para el curso de Python en coderhouse. 
# Cómo instalar y ejecutar el proyecto

Se debe crear el entorno virtual de python:
```bash
python -m venv venv
```

Luego activamos el entorno con el siguiente comando:
```bash
source venv\Scripts\activate
```
Luego procedemos a instalar los requerimientos:
```bash
pip install -r requirements.txt
```
Iniciamos nuestro proyecto.

```bash
cd proyecto_blog

python manage.py runserver
```
# Descripción
Como tematica para iniciar el proyecto final, me base en mi perro Milo, un bulldog frances de 8 años el cual conlleva muchos cuidados.

Cuenta con 2 apps:
1) AppBlog : contiene todo lo relacionado a los posteos.

2) AppRegistros: contiene todo lo relacionado con los usuarios y perfiles.

El superuser por defecto es:

  Username = admin

  Password = admin

- Es el único con la opción de ver, editar y borrar posteos.

Cada usuario creado tiene la posibilidad de ver todos los posteos, crear y solo editar los de su propia autoria.

La creacion de un post contiene:
1)  Título
2)  Descripción
3)  Categorías
4)  Contenido
5)  Imagen
  
En el navbar encontrara la opción de Post, Sobre mí y un menú desplegable que contara con el nombre del usuario logueado y entre sus opciones la posibilidad de ver su perfil y de cerrar sesión.
- El admin es el único que tendrá la opción para "Administrar el Blog".

Existe un buscador el cual obtendrá resultados dependiendo del título de cada posteo. A su vez existe un apartado de "Categorías" en donde están listadas todas las existentes, la cual, al hacer un click en cualquiera de ellas, redirecciona a los posteos de la categoría seleccionada.

En la parte de perfiles, cada usuario podrá subir una imagen a elección, editar su información personal y de contacto.

# 🔗 Links

www.linkedin.com/in/sebadimperio
