from django.shortcuts import render
from Blogs.models import Blog
# Create your views here.
def home(request):
    blogs= Blog.objects.all()
    contexto={
        'blogs' : blogs
    }
    return render(request, 'home.html', contexto)