from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm


def home(request):
    """Home page with published blog posts."""
    posts = Post.objects.filter(status='published').select_related('author', 'category')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)


def post_detail(request, slug):
    """Blog post detail view with comments."""
    post = get_object_or_404(Post, slug=slug, status='published')
    comments = post.comments.filter(is_active=True)
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('blog:post_detail', slug=slug)
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'title': post.title,
    }
    return render(request, 'blog/post_detail.html', context)


def category_posts(request, slug):
    """Posts filtered by category."""
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published').select_related('author', 'category')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
        'title': f'Category: {category.name}',
    }
    return render(request, 'blog/category_posts.html', context)


def search_posts(request):
    """Search blog posts."""
    query = request.GET.get('q', '')
    posts = Post.objects.filter(status='published')
    
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(excerpt__icontains=query)
        ).distinct()
    
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'query': query,
        'title': f'Search: {query}' if query else 'Search',
    }
    return render(request, 'blog/search_results.html', context)


@login_required
def create_post(request):
    """Create a new blog post."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    
    context = {
        'form': form,
        'title': 'Create Post',
    }
    return render(request, 'blog/create_post.html', context)


@login_required
def edit_post(request, slug):
    """Edit an existing blog post."""
    post = get_object_or_404(Post, slug=slug, author=request.user)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
        'title': 'Edit Post',
    }
    return render(request, 'blog/edit_post.html', context)


@login_required
def delete_post(request, slug):
    """Delete a blog post."""
    post = get_object_or_404(Post, slug=slug, author=request.user)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted!')
        return redirect('blog:home')
    
    context = {
        'post': post,
        'title': 'Delete Post',
    }
    return render(request, 'blog/delete_post.html', context)


@login_required
def my_posts(request):
    """View user's own posts."""
    posts = Post.objects.filter(author=request.user).select_related('category')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'title': 'My Posts',
    }
    return render(request, 'blog/my_posts.html', context)
