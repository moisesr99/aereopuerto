from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categoria(models.Model):
    nombre=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo=models.CharField(max_length=30)
    contenido=models.TextField(max_length=320)
    imagen=models.ImageField(upload_to="blog",null=True,blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    categorias=models.ManyToManyField(categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="post"
        verbose_name_plural="posts"
        
    def __str__(self):
        return self.titulo
