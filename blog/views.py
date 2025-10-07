from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost, Category
from .forms import BlogPostForm

@login_required
def create_blog_post(request):
    if request.user.user_type != 'doctor':
        messages.error(request, 'Only doctors can create blog posts.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('my_posts')
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def my_posts(request):
    if request.user.user_type != 'doctor':
        messages.error(request, 'Only doctors can view this page.')
        return redirect('dashboard')
    
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})

@login_required
def patient_blog_list(request):
    if request.user.user_type != 'patient':
        messages.error(request, 'Only patients can view this page.')
        return redirect('dashboard')
    
    categories = Category.objects.all()
    blogs_by_category = {}
    
    for category in categories:
        posts = BlogPost.objects.filter(category=category, is_draft=False)
        if posts.exists():
            blogs_by_category[category] = posts
    
    return render(request, 'blog/patient_blog_list.html', {'blogs_by_category': blogs_by_category})
