from django import forms
from .models import BlogPost, Category

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 3}),
            'content': forms.Textarea(attrs={'rows': 10}),
        }
        labels = {
            'is_draft': 'Save as Draft',
        }
