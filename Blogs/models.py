from django.db import models
from django.contrib.auth.models import User # Importa el modelo User

STATUS_CHOICES = (
    ('Draft', 'Draft'),     # 'Draft' para "Borrador"
    ('Published', 'Published'),  # 'Published' para "Publicado"
)


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories' # Para corregir la pluralización en el admin

    def __str__(self):
        return self.category_name    # ... (código existente de Category) ...

# Ahora define la clase Block (o Post)
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2500)
    status = models.CharField(choices=STATUS_CHOICES, max_length=25, default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# Create your models here.
