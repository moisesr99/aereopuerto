from django.shortcuts import render, redirect
from blog.models import Post, categoria
from django.contrib import messages
from datetime import date, datetime

# Create your views here.

def crear_post(request):
   posts=Post.objects.all()
   return render(request, "blog.html",{"posts":posts})

def publicar(request):
   
   if request.GET.get("titulo") and request.GET.get("descripcion") and request.GET.get("categoria"):
      blog_titulo = request.GET.get("titulo")
      blog_descripcion = request.GET.get("descripcion")
      blog_categoria = request.GET.get("categoria").upper()
      
      if len(blog_titulo) > 25:
         messages.error(request, 'Texto de titulo demadiaso largo')
         return redirect('crear_post')
      
      elif len(blog_descripcion) > 200:
         messages.error(request, 'Texto de descripcion demadiaso largo')
         return redirect('crear_post')
      
      elif len(blog_categoria) > 15:
         messages.error(request, 'Texto de categoria demadiaso largo')
         return redirect('crear_post')
      
      else:
         blog_subir = Post.objects.filter(categorias__icontains=blog_categoria)
         return render(request, "blog.html", {"cat":blog_subir})
         
      
   else:
      messages.error(request, "Error al subir el post")
      return redirect('crear_post') 
   
def categoria_view(request, categoria_id):
   filtro_categoria = categoria.objects.get(id=categoria_id)
   posts=Post.objects.filter(categorias=filtro_categoria)
   return render(request, "categorias.html", {"categoria":filtro_categoria,"posts":posts})