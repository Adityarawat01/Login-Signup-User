from django.contrib import admin
from .models import Category, BlogPost

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'is_draft', 'created_at']
    list_filter = ['category', 'is_draft', 'created_at']
    search_fields = ['title', 'content']
