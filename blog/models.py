from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_truncated_summary(self, word_limit=15):
        words = self.summary.split()
        if len(words) > word_limit:
            return ' '.join(words[:word_limit]) + '...'
        return self.summary
