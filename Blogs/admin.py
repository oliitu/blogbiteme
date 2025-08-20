from django.contrib import admin
from .models import Category, Blog

# Register your models here.
admin.site.register(Category)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status', 'is_featured') 
    search_fields = ('id', 'title', 'category__category_name', 'status') # 
    list_editable = ('is_featured',) # Campo editable directamente en la lista

admin.site.register(Blog, BlogAdmin)
